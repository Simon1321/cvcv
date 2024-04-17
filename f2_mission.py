import cv2
import numpy as np
import mission_ut as s


img = cv2.imread("f1.jpg")
result = cv2.blur(img, (5, 5))                                          #滤波操作
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)                         #灰度图转换
canny = cv2.Canny(img, 5, 10)                                           #边缘检测，以便后续圆的检测
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=80, param2=30, minRadius=15, maxRadius=100)      #霍夫检测

for circle in circles[0]:
    x = int(circle[0])
    y = int(circle[1])
    r = int(circle[2])
    img = cv2.circle(img, (x, y), r, (0, 255, 255), -1)

s.cv_show('img', img)
