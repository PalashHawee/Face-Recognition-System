from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime 
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Help
import tkinter
from chatbot import ChatBot


class Face_Recognition_System:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recongnition System")
	#First image section======	
		img=Image.open(r"D:\machine\img\varsity.jpg")
	#ANTIALIAS converts high level pic to low level	
		img=img.resize((500,130),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		f1_lbl=Label(self.root,image=self.photoimg)
		f1_lbl.place(x=0,y=0,width=500,height=130)
    #second image section======
		img1=Image.open(r"D:\machine\img\facialrecognition.png")
		
		img1=img1.resize((500,130),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		f1_lbl=Label(self.root,image=self.photoimg1)
		f1_lbl.place(x=500,y=0,width=500,height=130)
    #3rd image section=======
		img2=Image.open(r"D:\machine\img\clg.jpg")
		
		img2=img2.resize((500,130),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		f1_lbl=Label(self.root,image=self.photoimg2)
		f1_lbl.place(x=1000,y=0,width=550,height=130)

    #background image=======
		img3=Image.open(r"D:\machine\img\background.jpg")
		
		img3=img3.resize((1530,710),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=130,width=1530,height=710)
	#Title bar above background image======	
		title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Sketchy In Snow", 35,"bold"),bg="white",fg="black")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		#===========Time========
		def time():
			string=strftime('%H:%M:%S %p')
			lbl.config(text=string)
			lbl.after(1000,time)
		lbl=Label(title_lbl,font=('time new roman', 14, 'bold'),background='white', foreground='blue')
		lbl.place(x=0,y=0,width=110,height=50)
		time()	



	#student button====
		img4=Image.open(r"D:\machine\img\student.jpg")
		
		img4=img4.resize((220,220),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		b1=Button(bg_img,image=self.photoimg4, command=self.student_details,cursor="hand2")
		b1.place(x=200,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Student Details ", command=self.student_details,cursor="hand2",font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=200,y=300,width=220,height=40)

	#face detection button====
		img5=Image.open(r"D:\machine\img\face_detector1.jpg")
		
		img5=img5.resize((220,220),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		b1=Button(bg_img,image=self.photoimg5,cursor="hand2", command=self.face_data)
		b1.place(x=500,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Face Detector ",cursor="hand2",command=self.face_data,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=500,y=300,width=220,height=40)

	#Attendance detection button====
		img6=Image.open(r"D:\machine\img\smart-attendance.jpg")
		
		img6=img6.resize((220,220),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
		b1.place(x=800,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Attendance ",cursor="hand2",command=self.attendance_data,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=800,y=300,width=220,height=40)

	#Chat button====
		img7=Image.open(r"D:\machine\img\chatIcon.jpeg")
		
		img7=img7.resize((220,220),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.chatbot)
		b1.place(x=1100,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Chat Bot ",cursor="hand2",command=self.chatbot,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=1100,y=300,width=220,height=40)

	#Train button====
		img8=Image.open(r"D:\machine\img\train_data.jpg")
		
		img8=img8.resize((220,220),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		b1=Button(bg_img,image=self.photoimg8,cursor="hand2", command=self.train_data)
		b1.place(x=200,y=380,width=220,height=220)

		b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=200,y=580,width=220,height=40)

	#Photos button====
		img9=Image.open(r"D:\machine\img\photo.jpg")
		
		img9=img9.resize((220,220),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		b1=Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.open_img)
		b1.place(x=500,y=380,width=220,height=220)

		b1_1=Button(bg_img,text="Photos",cursor="hand2", command=self.open_img, font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=500,y=580,width=220,height=40)

	#Developer button====
		img10=Image.open(r"D:\machine\img\dev.jpg")
		
		img10=img10.resize((220,220),Image.ANTIALIAS)
		self.photoimg10=ImageTk.PhotoImage(img10)

		b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
		b1.place(x=800,y=380,width=220,height=220)

		b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=800,y=580,width=220,height=40)

	#Exit button====
		img11=Image.open(r"D:\machine\img\exit.jpg")
		
		img11=img11.resize((220,220),Image.ANTIALIAS)
		self.photoimg11=ImageTk.PhotoImage(img11)

		b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
		b1.place(x=1100,y=380,width=220,height=220)

		b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
		b1_1.place(x=1100,y=580,width=220,height=40)

	# Opening image function in photos section
	
	def open_img(self):
		os.startfile("data")

	#Exit func
	def iExit(self):
		self.iExit=tkinter.messagebox.askyesno("Face Recongnition","Are you sure to exit?",parent=self.root)
		if self.iExit > 0:
			self.root.destroy()
		else:
			return			

	#Function Buttons	

	def student_details(self):
		self.new_window=Toplevel(self.root)
		self.app=Student(self.new_window)

	#Train func
	def train_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Train(self.new_window)


	#Face Detector Func
	def face_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Face_Recognition(self.new_window)
	

		
	#Attendance Func
	def attendance_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Attendance(self.new_window)	


	#Developer Func
	def developer_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Developer(self.new_window)		



	#HelpDesk Func
	'''def help_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Help(self.new_window)'''

	#Chat bot
	def chatbot(self):
		self.new_window=Toplevel(self.root)
		self.app=ChatBot(self.new_window)			





if __name__=="__main__":
	root=Tk()
	obj=Face_Recognition_System(root)
	root.mainloop()








