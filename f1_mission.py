import cv2
import numpy as np
import mission_ut as s


img = cv2.imread("f2.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)								                #对原图进行灰度图转换
rest = cv2.GaussianBlur(img_gray, (5, 5), 1)                                                #高斯滤波
ret, thresh = cv2.threshold(rest, 127, 255, cv2.THRESH_BINARY)			                    #对灰度图进行二值化

kernel = np.ones((5,5),np.uint8)											                #开闭运算前的操作
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)					                #开运算

contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)	#绘制轮廓
cnt = contours[4]                                                                           #循环找到所求图像
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

s.cv_show('img',img)






