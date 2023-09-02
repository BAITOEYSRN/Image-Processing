import cv2
import numpy as np
import matplotlib.pyplot as plt
print(cv2.__version__)

cap = cv2.VideoCapture('video/MandM.mp4')
#cap = cv2.VideoCapture('video/test.mp4')
while (cap.isOpened()):
    check, frame = cap.read()  # รับภาพจาก video frame ต่อ frame
    scale = 50
    # ROWS =1080, COLS =1906
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    # counter
    counter_green = 0
    counter_orange = 0
    counter_red = 0
    counter_yellow = 0
    counter__blue = 0
    counter_brown = 0
    # HSV
    HSV = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    # green
    lower_green = np.array([38, 43, 0])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(HSV, lower_green, upper_green)
    res = cv2.bitwise_and(resized, resized, mask=mask)
    gray1 = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret, green = cv2.threshold(gray1, 50, 255, cv2.THRESH_BINARY)
    #kernel_green = np.ones((11, 11), np.uint8)
    #closing_green = cv2.morphologyEx(green, cv2.MORPH_CLOSE, kernel_green)
    contours, hierarchy = cv2.findContours(
        green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 1500 and area < 2600:  # 23,100
            ellipse_green = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_green, (0, 255, 0), 3)
            counter_green = counter_green+1

            if counter_green > 2:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

        elif area > 2600:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_green = counter_green+1
            cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # orange
    lower_orange = np.array([0, 94, 109])
    upper_orange = np.array([14, 255, 255])
    mask = cv2.inRange(HSV, lower_orange, upper_orange)
    res01 = cv2.bitwise_and(resized, resized, mask=mask)
    gray02 = cv2.cvtColor(res01, cv2.COLOR_BGR2GRAY)
    ret, threshold1 = cv2.threshold(gray02, 60, 255, cv2.THRESH_TOZERO)
    ret, orange = cv2.threshold(threshold1, 30, 255, cv2.THRESH_BINARY)
    kernel_orange = np.ones((3, 3), np.uint8)
    kernel_orange1 = np.ones((15, 15), np.uint8)
    opening_orange = cv2.morphologyEx(orange, cv2.MORPH_OPEN, kernel_orange)
    closing_orange = cv2.morphologyEx(
        opening_orange, cv2.MORPH_CLOSE, kernel_orange1)
    contours, hierarchy = cv2.findContours(
        orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1500 and area < 2450:  # 23,100
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_orange = counter_orange+1
            if counter_orange > 1:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

        elif area > 2450:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_orange = counter_orange+1
            if counter_orange > 1:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # red
    lower_red = np.array([0, 173, 0])
    upper_red = np.array([1, 255, 255])
    mask = cv2.inRange(HSV, lower_red, upper_red)
    res1 = cv2.bitwise_and(resized, resized, mask=mask)
    gray2 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
    ret, red = cv2.threshold(gray2, 10, 255, cv2.THRESH_BINARY)
    kernel_red = np.ones((25, 25), np.uint8)
    kernel_red1 = np.ones((5, 5), np.uint8)
    closing_red = cv2.morphologyEx(red, cv2.MORPH_CLOSE, kernel_red)
    opening_red = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernel_red1)

    contours, hierarchy = cv2.findContours(
        closing_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1500 and area < 2500:  # 23,100
            ellipse_red = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_red, (0, 0, 255), 3)
            counter_red = counter_red+1
            if counter_red > 2:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
        elif area > 2500:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_red = counter_red+1
            cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    lower_yellow = np.array([16, 180, 0])
    upper_yellow = np.array([35, 255, 255])
    mask = cv2.inRange(HSV, lower_yellow, upper_yellow)
    res3 = cv2.bitwise_and(resized, resized, mask=mask)
    gray3 = cv2.cvtColor(res3, cv2.COLOR_BGR2GRAY)
    ret, yellow = cv2.threshold(gray3, 10, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    closing_yellow = cv2.morphologyEx(yellow, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy = cv2.findContours(
        yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1400 and area < 2500:  # 23,100
            ellipse_yellow = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_yellow, (0, 255, 255), 3)
            counter_yellow = counter_yellow+1
            if counter_yellow > 2:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
        elif area > 2500:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_yellow = counter_yellow+1
            cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # blue เพิ่ม fill holes
    lower_blue = np.array([94, 99, 0])
    upper_blue = np.array([128, 255, 255])
    mask = cv2.inRange(HSV, lower_blue, upper_blue)
    res4 = cv2.bitwise_and(resized, resized, mask=mask)
    gray4 = cv2.cvtColor(res4, cv2.COLOR_BGR2GRAY)
    ret, blue = cv2.threshold(gray4, 20, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1500 and area < 2500:  # 23,100
            ellipse_blue = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_blue, (255, 0, 0), 3)
            counter__blue = counter__blue+1
            if counter__blue > 2:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
        elif area > 2500:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter__blue = counter__blue+1
            cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # brown เพิ่มขอบ
    lower_brown = np.array([0, 62, 0])
    upper_brown = np.array([16, 239, 59])
    mask = cv2.inRange(HSV, lower_brown, upper_brown)
    res5 = cv2.bitwise_and(resized, resized, mask=mask)
    gray5 = cv2.cvtColor(res5, cv2.COLOR_BGR2GRAY)
    ret, brown = cv2.threshold(gray5, 5, 255, cv2.THRESH_BINARY)
    kernel_brown = np.ones((9, 9), np.uint8)
    closing = cv2.morphologyEx(brown, cv2.MORPH_CLOSE, kernel_brown)
    contours, hierarchy = cv2.findContours(
        brown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1500 and area < 2500:  # 23,100
            ellipse_brown = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_brown, (0, 76, 153), 3)
            counter_brown = counter_brown+1
            if counter_brown > 2:
                cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)
        elif area > 2500:
            ellipse_orange = cv2.fitEllipse(cnt)
            cv2.ellipse(resized, ellipse_orange, (0, 0, 0), 3)
            counter_brown = counter_brown+1
            cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    total = counter_yellow + counter_red + counter__blue + \
        counter_green + counter_brown + counter_orange

    cv2.putText(resized, 'Yellow: ' + str(counter_yellow), (10, 100),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
    cv2.putText(resized, 'Red  : ' + str(counter_red), (10, 150),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    cv2.putText(resized, 'Blue  : ' + str(counter__blue), (10, 250),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
    cv2.putText(resized, 'Green  : ' + str(counter_green), (10, 300),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 3)
    cv2.putText(resized, 'Brown  : ' + str(counter_brown), (10, 350),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 76, 153), 2)
    cv2.putText(resized, 'Orange  : ' + str(counter_orange), (10, 200),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 128, 255), 2)
    cv2.putText(resized, 'Total  : ' + str(total), (10, 400),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 128, 255), 2)

    if total == 10:
        if counter_yellow == 2:
            if counter_red == 2:
                if counter__blue == 2:
                    if counter_green == 2:
                        if counter_brown == 2:
                            cv2.putText(resized, 'Result  : ' + str("PASS"), (10, 450),
                                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    elif total > 1 or total < 10 or total > 10:
        cv2.putText(resized, 'Result  : ' + str("FAIL"), (10, 500),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

    else:
        cv2.putText(resized, 'Result  : ', (10, 500),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2, cv2.LINE_AA)

#    cv2.imshow('original', frame)
#    cv2.imshow('HSV', HSV)
    cv2.imshow('video', resized)
#    cv2.imshow('green', res)
#    cv2.imshow('closing_green', closing_green)
    cv2.imshow('green', green)
#    cv2.imshow('threshold1', orange)
#    cv2.imshow('opening_orange', opening_orange)
#    cv2.imshow('threshold1', threshold1)
#    cv2.imshow('threshold', orange)
#    cv2.imshow('closing_orange', closing_orange)
#    cv2.imshow('red', res1)
#    cv2.imshow('red', red)
#    cv2.imshow('closing_red', closing_red)
 #   cv2.imshow('open', opening_red)
#    cv2.imshow('closing', closing)
#    cv2.imshow('yellow', res3)
#    cv2.imshow('yellow', yellow)
#    cv2.imshow('closing_yellow', closing_yellow)
#    cv2.imshow('blue', res4)
#    cv2.imshow('blue', blue)
#    cv2.imshow('brown', res5)
#    cv2.imshow('brown', brown)
#    cv2.imshow('closing', closing)

    if cv2.waitKey(5) & 0xFF == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
