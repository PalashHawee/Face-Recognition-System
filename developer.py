from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Developer:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recongnition System")



		title_lbl=Label(self.root,text="DEVELOPER",font=("Sketchy In Snow", 35,"bold"),bg="darkgreen",fg="red")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		#Image in top bar
		img_top=Image.open(r"D:\machine\img\developerImg.jpg")
		
		img_top=img_top.resize((1530,720),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		f_lbl=Label(self.root,image=self.photoimg_top)
		f_lbl.place(x=0,y=55,width=1530,height=720) 



		#Frame
		main_frame=Frame(f_lbl,bd=2,bg="white")
		main_frame.place(x=1000,y=0,width=500,height=600)

		img_top1=Image.open(r"D:\machine\img\devPic.jpg")
		
		img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
		self.photoimg_top1=ImageTk.PhotoImage(img_top1)

		f_lbl=Label(main_frame,image=self.photoimg_top1)
		f_lbl.place(x=300,y=0,width=200,height=200) 

		#Developer Info
		def callback(url):
			webbrowser.open_new(url)
		dev_label=Label(main_frame,text="Hello, this is Palash Hawee",font=("times new roman",15,"bold"),bg="white")
		dev_label.place(x=0,y=50)

		dev_label=Label(main_frame,text="I'm an aspiring Software Engineer",font=("times new roman",15,"bold"),bg="white")
		dev_label.place(x=0,y=100)

		dev_label=Label(main_frame,text="A student of Bangalore University",font=("times new roman",15,"bold"),bg="white")
		dev_label.place(x=0,y=150)

		dev_label1=Label(main_frame,text="My GitHub: Palash Hawee", fg="blue", cursor="hand2")
		dev_label1.place(x=0,y=300)
		dev_label1.pack()
		dev_label1.bind("<Button-1>", lambda e: callback("https://github.com/PalashHawee"))

		
		dev_label2=Label(main_frame,text="My LinkedIn: Palash Hawee", fg="blue", cursor="hand2")
		dev_label2.place(x=0,y=350)
		dev_label2.pack()
		dev_label2.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/palash-hawee/"))





if __name__=="__main__":
	root=Tk()
	obj=Developer(root)
	root.mainloop()			