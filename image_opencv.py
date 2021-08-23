import cv2

case_path = cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml'
# eyeCascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier(case_path)
image = cv2.imread('C:\\OPENCV\\photo\\2.jpg')
image_re = cv2.resize(image,(700,500),interpolation = cv2.INTER_AREA)
cv2.imshow('peo',image_re)
cv2.waitKey(0)
# print(image_re.shape)
##偵測臉部
# cv2.imwrite('C:\OPENCV\img_1.jpg',image_re)
faces = faceCascade.detectMultiScale (image_re
,scaleFactor = 1.1,minNeighbors =3,minSize=(50,0)
,flags=cv2.CASCADE_SCALE_IMAGE)
# print((faces))
imgheight= image_re.shape[0]
imgwidth = image_re.shape[1]

##儲存個人臉部
count = 1
for (x,y,w,h) in faces:
    cv2.rectangle(image_re,(x,y),(x+w,y+h),(255,0,0),2) # 綠框與粗度
    filename = 'C:\OPENCV\people\img_'+str(count)+'.jpg'
    image1 = image_re[y:y+h,x:x+w]
    image2 = cv2.resize(image1,(200,200))
    cv2.imwrite(filename,image2)
    count += 1

cv2.namedWindow('facedetect')
cv2.imshow('facedetect',image_re)
cv2.waitKey(0)
cv2.destroyWindow('facedetect')



# # 選擇第二隻攝影機
# cap = cv2.VideoCapture(0)

# while True:
#   # 從攝影機擷取一張影像
#   ret, frame = cap.read()

#   # 顯示圖片
#   cv2.imshow('frame', frame)

#   # 若按下 q 鍵則離開迴圈
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# # 釋放攝影機
# cap.release()

# # 關閉所有 OpenCV 視窗
# cv2.destroyAllWindows()