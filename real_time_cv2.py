import cv2
import numpy as np
import os 
import glob
from boltiot import Sms

SID = "AC1e6ceaae1d533c27ae4eb1e2577a6e3b"

AUTH = "ac5c78ad809c724b3409715917dfbd4d"

FROM = "(863) 532-4946"

TO = "+919116623976"

sms = Sms(SID, AUTH, TO, FROM)


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml') # train my face using LPBH Algorithm
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
ids = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names  = ["Aman", "Suhani", "Hema"] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH))
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        ids, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            ids = names[ids]
            sms.send_sms("""


    
            	{}""".format(ids))
        else:
            ids = "unknown"
        
        cv2.putText(img, ids, (x+5,y-5), font, 1, (255,255,255), 2)
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()