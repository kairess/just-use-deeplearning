import cv2

cap = cv2.VideoCapture('03.mp4')

while True:
    ret, img = cap.read()

    if not ret:
        break

    cv2.rectangle(img, pt1=(721, 183), pt2=(878, 465), color=(255, 0, 0), thickness=2)

    cropped_img = img[183:465, 721:878]

    cv2.imshow('cropped_img', cropped_img)
    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break
