import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/eccv16/starry_night.t7')

img = cv2.imread('imgs/01.jpg')

h, w, c = img.shape

MEAN_VALUE = [103.939, 116.779, 123.680]
IMG_SIZE = 640

blob = cv2.dnn.blobFromImage(img, size=(640, int(h / w * 640)), mean=MEAN_VALUE)

net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))

output += MEAN_VALUE
output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imshow('img', img)
cv2.imshow('result', output)
cv2.waitKey(0)
