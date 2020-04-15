import cv2
import os
from os import path
import shutil  
from config import n, max1

file_name1 = "image"


face_cascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")
if os.path.isdir(file_name1):	
	shutil.rmtree(file_name1)

os.mkdir(file_name1)
count1 = ""

for i in range(n):
	count = 0


	os.system("clear")

	print("________________________________________________")

	name = input("Enter Your Name (DO NOT SPACE) Only ONE Word :")
	print("________________________________________________\n\n")


	print("____________________LOADING...________________")

	input("are you ready for take Pic,"+name+"?")


	def detect(frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		faces = face_cascade.detectMultiScale(gray, 1.5,5)

		if faces is ():
			return None
		else:
			for x,y,w,h in faces:
				return (x,y,w,h)


	cap = cv2.VideoCapture(0)
	while True:
		file_name = file_name1+"/"+name

		if not path.isdir(file_name):
			os.mkdir(file_name)
			pass

		_, frame = cap.read()


		if detect(frame) is not None:
			x,y,w,h = detect(frame)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
			count += 1

			face = frame[y:y+h, x:x+w]
			face = cv2.resize(face, (128, 128))
			face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)


			cv2.imwrite("{}/{}/{}.{}.jpg".format(file_name1,name,name,count), face_gray)

			count1 = ""
		else:
			count1 = "  face not found!!!"

			pass

		cv2.putText(frame, str(count)+str(count1), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

		cv2.imshow("video",frame)

		k = cv2.waitKey(30) & 0xff
		if k == 27 or count >= max1: 	# press 'ESC' to quit
			break

	cap.release()
	cv2.destroyAllWindows()
