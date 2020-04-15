import cv2
import glob
max1 = 500
import numpy as np

train = []
labels = []

names  = [] 
a = glob.glob("image/*")
b = " ".join(a).split(" ")
for i in b:
	names.append(i.split('\\')[1])

print(names)






for num,name in enumerate(names):
	for i in range(1,max1):
	    a = cv2.imread("image/"+name+"/"+name+".{}.jpg".format(i))
	    gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	    labels.append(num)
	    train.append(gray)
    

train = np.array(train)
labels = np.array(labels)

train = train/255.0


face_cascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")


recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(train, labels)

recognizer.write('trainer.yml')