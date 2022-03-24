#!/usr/bin/env python3
import rospy
import time
from PIL import Image
from sensor_msgs.msg import Image as ROSImage
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
import socket

import numpy as np
import tflite_runtime.interpreter as tflite
model = "./ssd_mobilenet_v1_1_metadata_1.tflite"
interpreter = tflite.Interpreter(model_path=model, num_threads=4)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape']

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = '10.0.0.2', 10000

def callback(data):
    start_ms = int( time.time_ns() / 1000 )
    rgb_image = CvBridge().imgmsg_to_cv2(data, desired_encoding="rgb8")
    im = Image.fromarray(rgb_image)

    # begin tensorflow stuff
    res_im = im.resize((300, 300))
    np_res_im = np.array(res_im)
    np_res_im = (np_res_im).astype('uint8')
    if len(np_res_im.shape) == 3:
        np_res_im = np.expand_dims(np_res_im, 0)
    
    input_data = np_res_im
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    outputLocations = interpreter.get_tensor(output_details[0]['index'])
    outputClasses = interpreter.get_tensor(output_details[1]['index'])
    outputScores = interpreter.get_tensor(output_details[2]['index'])
    numDetections = interpreter.get_tensor(output_details[3]['index'])

    label_names = [line.rstrip('\n') for line in open("labelmap.txt")]
    label_names = np.array(label_names)
    numDetectionsOutput = int(np.minimum(numDetections[0],10))

    inputSize = 300
    dogFound = False
    for i in range(numDetectionsOutput):
        if dogFound == False:
            class_name = label_names[int(outputClasses[0][i])]
            if class_name == "person": ### CHANGE THIS TO DOG IN PRODUCTION
                dogFound = True
                talker(start_ms, class_name, str(outputScores[0][i]), str(outputLocations[0][i][1]), str(outputLocations[0][i][0]), str(outputLocations[0][i][3]), str(outputLocations[0][i][2]))

def talker(start_ms, class_name, confidence, x_min, y_min, x_max, y_max):
    pub = rospy.Publisher('/bbox/' + class_name, String)
    latency = int( time.time_ns() / 1000 ) - start_ms
    outputmessage = str(latency) + "/" + x_min + "/" + y_min + "/" + x_max + "/" + y_max
    logic(outputmessage)
    rospy.loginfo(outputmessage)
    pub.publish(outputmessage)

def logic(message): # we are passing delimited message because this might move out of here
    time, x_min, y_min, x_max, y_max = message.split('/')
    x_avg = (float(x_min) + float(x_max))/2
    height = float(y_max) - float(y_min)
    motor_L = 0
    motor_R = 0
    if x_avg < 0.3:
        print("Turn left")
        throttle = (1-x_avg)*5
        motor_L = -throttle
        motor_R = throttle
    elif x_avg > 0.7:
        print("Turn right")
        throttle = x_avg*5
        motor_L = throttle
        motor_R = -throttle
    print(x_avg, height)
    packaged = str(motor_L) + '/' + str(motor_R)
    s.sendto(packaged.encode(), target)

def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera/rgb/image_color", ROSImage, callback, queue_size=1)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()