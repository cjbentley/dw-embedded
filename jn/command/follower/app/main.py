#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    ### Please note: this is outdated code below. 
    ### Currently the logic section is implemented in the tf container for ease of testing!
    ### Once the setup is more stable, it will be moved to this bouncer container.

    # time, x_min, y_min, x_max, y_max = message.split('/')
    # x_avg = (float(x_min) + float(x_max))/2
    # height = float(y_max) - float(y_min)
    # if x_avg < 0.5:
    #     print("Turn left")
    # elif x_avg > 0.5:
    #     print("Turn right")
    # print(x_avg, height)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/bbox", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()