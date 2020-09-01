import cv2

img = cv2.imread('01.jpg')

cv2.rectangle(img, pt1=(259, 89), pt2=(380, 348), color=(255, 0, 0), thickness=2)
cv2.circle(img, center=(320, 220), radius=100, color=(255, 0, 0), thickness=2)

cropped_img = img[89:348, 259:380]

cv2.imshow('cropped', cropped_img)
cv2.imshow('result', img)
cv2.waitKey(0)
