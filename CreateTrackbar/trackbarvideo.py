import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture('MandM.mp4')

cv2.namedWindow('Tracking')
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange) # สร้างบาร์ติดตามสำหรับการเปลี่ยนสี
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while (cap.isOpened()):

    check, frame = cap.read()  # รับภาพจาก video frame ต่อ frame
    scale = 40
    # ROWS =1080, COLS =1906
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # HSV
    HSV = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    LH = cv2.getTrackbarPos("LH", "Tracking")
    LS = cv2.getTrackbarPos("LS", "Tracking")
    LV = cv2.getTrackbarPos("LV", "Tracking")

    UH = cv2.getTrackbarPos("UH", "Tracking")
    US = cv2.getTrackbarPos("US", "Tracking")
    UV = cv2.getTrackbarPos("UV", "Tracking")

    lower = np.array([LH, LS, LV])
    upper = np.array([UH, US, UV])
    mask = cv2.inRange(HSV, lower, upper)
    res5 = cv2.bitwise_and(resized, resized, mask=mask)

    cv2.imshow('video', resized)
    cv2.imshow('HSV', res5)
    if cv2.waitKey(30) & 0xFF == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
