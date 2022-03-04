import numpy as np
import tflite_runtime.interpreter as tflite

model = "./ssd_mobilenet_v1_1_metadata_1.tflite"
interpreter = tflite.Interpreter(model_path=model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

from PIL import Image
im = Image.open("testimage.jpg")
res_im = im.resize((300, 300))
np_res_im = np.array(res_im)
np_res_im = (np_res_im).astype('uint8')
if len(np_res_im.shape) == 3:
    np_res_im = np.expand_dims(np_res_im, 0)

input_shape = input_details[0]['shape']
input_data = np_res_im
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

outputLocations = interpreter.get_tensor(output_details[0]['index'])
print(outputLocations.shape)
outputClasses = interpreter.get_tensor(output_details[1]['index'])
print(outputClasses.shape)
outputScores = interpreter.get_tensor(output_details[2]['index'])
print(outputScores.shape)
numDetections = interpreter.get_tensor(output_details[3]['index'])
print(numDetections.shape)

label_names = [line.rstrip('\n') for line in open("labelmap.txt")]
label_names = np.array(label_names)
numDetectionsOutput = int(np.minimum(numDetections[0],10))


import matplotlib.pyplot as plt
import matplotlib.patches as patches

for i in range(numDetectionsOutput):
    # Create figure and axes
    fig, ax = plt.subplots()
    # Display the image
    ax.imshow(res_im)
    # Create a Rectangle patch
    inputSize = 300
    left = outputLocations[0][i][1] * inputSize
    top = outputLocations[0][i][0] * inputSize
    right = outputLocations[0][i][3] * inputSize
    bottom = outputLocations[0][i][2] * inputSize
    class_name = label_names[int(outputClasses[0][i])]
    print("Output class: "+class_name+" | Confidence: "+ str(outputScores[0][i]))
    rect = patches.Rectangle((left, bottom), right-left, top-bottom, linewidth=1, edgecolor='r', facecolor='none')
    # Add the patch to the Axes
    ax.add_patch(rect)
    plt.show()