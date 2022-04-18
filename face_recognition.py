from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recongnition System")

		title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Sketchy In Snow", 35,"bold"),bg="white",fg="green")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		#Image in top bar
		img_top=Image.open(r"D:\machine\img\face_detector1.jpg")
		
		img_top=img_top.resize((650,700),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		f_lbl=Label(self.root,image=self.photoimg_top)
		f_lbl.place(x=0,y=55,width=650,height=700) 


		#Image in side right bar
		img_bottom=Image.open(r"D:\machine\img\face.jpg")
		
		img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
		self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

		f_lbl=Label(self.root,image=self.photoimg_bottom)
		f_lbl.place(x=650,y=55,width=950,height=700) 

		#button
		b1_1=Button(f_lbl,text="Face Recongnition", command=self.face_recog,cursor="hand2",font=("times new roman", 18,"bold"),bg="red",fg="white")
		b1_1.place(x=365,y=620,width=200,height=40)

	#========Attendance========
	def mark_attendance(self,i,r,n,d):
		with open("MyTest.csv","r+",newline="\n") as f:
			myDataList=f.readlines()
			name_list=[]
			for line in myDataList:
				entry=line.split((","))
				name_list.append(entry[0])
			if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
				now=datetime.now()
				d1=now.strftime("%d/%m/%Y")
				dtString=now.strftime("%H:%M:%S")
				f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


	#=======face recognition=====
	def face_recog(self):
		def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
			gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

			coord=[]
			for (x,y,w,h) in features:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
				id,predict=clf.predict(gray_image[y:y+h,x:x+w])
				confidence=int((100*(1-predict/300)))

				conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
				my_cursor=conn.cursor()

				#For department fetching
				my_cursor.execute("SELECT Student_id FROM student WHERE Student_id="+str(id))
				i=my_cursor.fetchone()
				i="+".join(i)

				'''#For course fetching
				my_cursor.execute("select course from student where Student_id="+str(id))
				c=my_cursor.fetchone()
				c="+".join(c)

				#For year fetching
				my_cursor.execute("select Year from student where Student_id="+str(id))
				y=my_cursor.fetchone()
				y="+".join(y)

				#For semester fetching
				my_cursor.execute("select Semester from student where Student_id="+str(id))
				s=my_cursor.fetchone()
				s="+".join(s)
				'''
				#Fetching Name
				my_cursor.execute("SELECT Reg FROM student WHERE Student_id="+str(id))
				r=my_cursor.fetchone()
				r="+".join(r)


				#Fetching registration
				my_cursor.execute("SELECT Name FROM student WHERE Student_id="+str(id))
				n=my_cursor.fetchone()
				n="+".join(n)

				#Fetching Student ID
				my_cursor.execute("SELECT Dep FROM student WHERE Student_id="+str(id))
				d=my_cursor.fetchone()
				d="+".join(d)
				
				if confidence>77:
					cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					cv2.putText(img,f"Registration:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					#cv2.putText(img,f"Semester:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					self.mark_attendance(i,r,n,d)
				
				#If face doesn't match	
				else:
					cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
					cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
				coord=[x,y,w,h]
			return coord
		
		def recognize(img,clf,faceCascade):
			coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)

			return img
		faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.read("classifier.xml")

		video_cap=cv2.VideoCapture(0) # it was 0 inside

		while True:
			ret,img=video_cap.read()
			img=recognize(img,clf,faceCascade)
			cv2.imshow("Welcome to Face Recongnition",img)

			if cv2.waitKey(1)==13:
				break
		video_cap.release()
		cv2.destroyAllWindows()			



					

					





if __name__=="__main__":
	root=Tk()
	obj=Face_Recognition(root)
	root.mainloop()			