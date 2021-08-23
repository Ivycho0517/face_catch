import cv2 as cv
import numpy as np
img = cv.imread('C:/OPENCV/photo/boston.jpg')
#顯示圖片
#cv.imshow('boston',img)
#關閉圖片秒數

# 定義圖片平移
def translate(img,x,y):
    # x軸平移x,y軸平移y
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

translated = translate (img,400,-400)
# cv.imshow('translated',translated)
# cv.waitKey(0)

# 定義圖片旋轉
def rotate (img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width/2,height/2) # 圖片中心

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height) # 參數縮放比例
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,-90)

#rotated_rotated = rotate (rotated,-70)
#rotated_a=rotate (img,-90)

#cv.imshow('rotated',rotated)

# resizing

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

#cv.imshow('resized',resized)

# 翻轉
# 1:橫向 0:縱向 -1:橫縱向
flip =cv.flip(img,-1) 
cv.imshow('flip',flip)
cv.waitKey(0)


