import cv2
import numpy as np
import mission_ut as s

img=cv2.imread("f3.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_r = np.array([0, 100, 100])                       # 红色阈值下界
upper_r = np.array([10, 255, 255])                      # 红色阈值上界
mask2 = cv2.inRange(hsv, lower_r, upper_r)              #设置掩码
rest = cv2.bitwise_and(img, img, mask = mask2)
rectangle = np.where(mask2 == 255)
cv2.rectangle(img, (min(rectangle[1]), min(rectangle[0])), (max(rectangle[1]), max(rectangle[0])), (123, 158, 158), 2)

s.cv_show('img',img)



