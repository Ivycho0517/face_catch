import cv2 as cv
import numpy as np
####################
#     讀取圖檔      #
####################
# 讀取圖片
#img = cv.imread('C:/OPENCV/photo/cat.jpg')
# 顯示圖片
# cv.imshow('cat',img)
# 關閉圖片秒數
# cv.waitKey(0)
# cv.destroyAllWindows()
####################
#      大小調整     #
####################
# 定義縮放


def rescaleFrame(Frame, scale=0.50):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(Frame, dimensions)


# 出示圖片
img = cv.imread('C:\OPENCV\photo\cat.jpg')
#frame_resized = rescaleFrame(img)
# cv.imshow('resize_cat',frame_resized)
# cv.waitKey(0)

####################
#      基本技巧     #
####################
# 轉灰階
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray_cat',gray)
# cv.waitKey(0)
# 模糊
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur_cat',blur)
# cv.waitKey(0)
# 描邊
canny = cv.Canny(gray, 125, 175)  # 輸入的圖片必須是灰階
# cv.imshow('canny_cat',canny)
# 侵蝕、膨脹
# erode 先侵蝕以去噪，再用dilate膨脹
dilated = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow('dilated',dilated)
erode = cv.erode(dilated, (7, 7), iterations=1)
# cv.imshow('erode',erode)
# cv.waitKey(0)
# resize
resize = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC)
# cv.imshow('resize',resize)
# crop 裁切
cropped = img[50:100, 40:80]  # x軸與長度,y軸與長度
cv.imshow('cropped', cropped)
cv.waitKey(0)
