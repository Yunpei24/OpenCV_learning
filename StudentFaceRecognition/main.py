import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 648)
cap.set(4, 480)

imgBackground = cv2.imread('Ressources/background.png')

while True:
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img

    cv2.imshow("Webcam", img)
    cv2.imshow('Face Attendance', imgBackground)
    cv2.waitKey(1)