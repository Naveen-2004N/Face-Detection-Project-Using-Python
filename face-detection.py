import cv2
face_detection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_detection.detectMultiScale(gray,1.3,6,minSize=(100,100))
    for (x,y,w,h) in face:
            cv2.rectangle(frame,
                  (x,y),(x+w,y+h),(255,0,0,2))
    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(1) == ord("a"):
          break
video.release()
cv2.destroyAllWindows()