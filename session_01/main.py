import cv2

cap = cv2.VideoCapture('01.mp4')

while True:
    ret, img = cap.read()

    if not ret:
        break

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break
