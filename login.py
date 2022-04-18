from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
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

#For common object for both classes

def main():
	win=Tk()
	app=Login_window(win)
	win.mainloop()


class Login_window(object):
	"""docstring for login"""
	def __init__(self, root):
		self.root=root
		self.root.title("Login")
		self.root.geometry("1550x800+0+0")

		#Image
		self.bg=ImageTk.PhotoImage(file=r"D:\machine\img\LoginImg.jpg")

		lbl_bg=Label(self.root,image=self.bg)
		lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)  #rel for automatic fit the image whenever login

		#Farme for login field
		frame=Frame(self.root,bg="black")
		frame.place(x=610,y=170,width=340,height=450)

		img1=Image.open(r"D:\machine\img\loginIcon.png")
		img1=img1.resize((100,100),Image.ANTIALIAS)
		self.photoimage1=ImageTk.PhotoImage(img1)
		lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
		lblimg1.place(x=730,y=175,width=100,height=100)

		get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="white",bg="black")
		get_str.place(x=95,y=100)

		#Labels for user and password
		username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
		username.place(x=70,y=155)

		self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.txtuser.place(x=40,y=180,width=270)


		#For password label
		password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
		password.place(x=70,y=225)

		self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
		self.txtpass.place(x=40,y=250,width=270)

		#=======Icon Images=====
		img2=Image.open(r"D:\machine\img\customerUser.png")
		img2=img2.resize((25,25),Image.ANTIALIAS)
		self.photoimage2=ImageTk.PhotoImage(img2)
		lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
		lblimg1.place(x=650,y=323,width=25,height=25)


		#======Password Icon=====
		img3=Image.open(r"D:\machine\img\passwordIc.png")
		img3=img3.resize((25,25),Image.ANTIALIAS)
		self.photoimage3=ImageTk.PhotoImage(img3)
		lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
		lblimg1.place(x=650,y=395,width=25,height=25)


		#=====log in button=====
		loginbtn=Button(frame,text="Login", command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
		loginbtn.place(x=110,y=330,width=120,height=35)


		#=====Register button=====
		registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
		registerbtn.place(x=15,y=370,width=160)


		#=====Forget password button=====
		loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
		loginbtn.place(x=10,y=390,width=160)

	#For new user func
	def register_window(self):
		self.new_window=Toplevel(self.root)
		self.app=Register(self.new_window)	


	#Log in function	
	def login(self):
		if self.txtuser.get()=="" or self.txtpass.get()=="":
			messagebox.showerror("Error", "all fields required")
		elif self.txtuser.get()=="palash" and self.txtpass.get()=="123":
			messagebox.showinfo("Success", "Welcome to Face Recognition System")
		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")			
			my_cursor=conn.cursor()
			my_cursor.execute("select * from register where email=%s and password=%s",(
																						self.txtuser.get(),
																						self.txtpass.get()
																					))
			row=my_cursor.fetchone()
			if row==None:
				messagebox.showerror("Error", "Invalid Username & Password")
			else:
				open_main=messagebox.askyesno("YesNo", "Access only Admin")
				if open_main > 0:
					self.new_window=Toplevel(self.root)
					self.app=Face_Recognition_System(self.new_window)

				else:
					if not open_main:
						return
			conn.commit()
			conn.close()



	#==================Reset Button Function=============
	def reset_pass(self):
		if self.combo_security_Q.get()=="Select":
			messagebox.showerror("Error", "Select Security Question",parent=self.root2)
		elif self.txt_security.get()=="":
			messagebox.showerror("Error", "Please give the Answer",parent=self.root2)

		elif self.txt_newpass.get=="":
			messagebox.showerror("Error", "Please eneter the  new password",parent=self.root2)

		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")			
			my_cursor=conn.cursor()
			query=("select * from register where email=%s and securityQ=%s and securityA=%s")
			value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),) 
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()

			#Check if the answer is correct
			if row==None:
				messagebox.showerror("Error", "Please enter the correct Answer",parent=self.root2)
			else:
				query=("update register set password=%s where email=%s")	
				value=(self.txt_newpass.get(),self.txtuser.get())
				my_cursor.execute(query,value)

				conn.commit()
				conn.close()
				messagebox.showinfo("Info", "Your password has been reset, please login with new password ",parent=self.root2)	

				self.root2.destroy()

	#======forget password function=========
	def forgot_password_window(self):
		if self.txtuser.get()=="":
			messagebox.showerror("Error", "Please enter the Email address to reset password")
		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")			
			my_cursor=conn.cursor()
			query=("select * from register where email=%s")
			value=(self.txtuser.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()

			#For correct user name or email
			if row==None:
				messagebox.showerror("My Error", "Please enter the valid user name")
			#Opening new window if correct email
			else:
				conn.close()
				self.root2=Toplevel()
				self.root2.title("Forget Password")
				self.root2.geometry("340x450+610+170")

				l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
				l.place(x=0,y=10,relwidth=1)	

				security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
				security_Q.place(x=50,y=80)

				self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
				self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend Name","Your Favourite food")
				self.combo_security_Q.place(x=50,y=110,width=250)
				self.combo_security_Q.current(0)

				security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
				security_A.place(x=50,y=150)

				self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
				self.txt_security.place(x=50,y=180,width=250)

				new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
				new_password.place(x=50,y=220)

				self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
				self.txt_newpass.place(x=50,y=250,width=250)

				#reset button
				btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
				btn.place(x=100,y=290)


												

			

			

# Copied from Register page

class Register:
	def __init__(self, root):
		self.root=root
		self.root.title("Register")
		self.root.geometry("1600x900+0+0")

		#==========Variables=====
		self.var_fname=StringVar()
		self.var_lname=StringVar()
		self.var_contact=StringVar()
		self.var_email=StringVar()
		self.var_securityQ=StringVar()
		self.var_securityA=StringVar()
		self.var_pass=StringVar()
		self.var_confpass=StringVar()

		#=======Bg Image====
		self.bg=ImageTk.PhotoImage(file=r"D:\machine\img\background.jpg")

		lbl_bg=Label(self.root,image=self.bg)
		lbl_bg.place(x=0,y=0,relwidth=1,relheight=1) 

		#====left image=====
		self.bg1=ImageTk.PhotoImage(file=r"D:\machine\img\regLeft.jpg")

		left_lbl=Label(self.root,image=self.bg1)
		left_lbl.place(x=50,y=100,width=470,height=550) 

		#Frame
		frame=Frame(self.root,bg="white")
		frame.place(x=510,y=100,width=800,height=550)


		#Register Label
		register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman ",20,"bold"),fg="green",bg="white")
		register_lbl.place(x=20,y=20)

		#====Label and Entry====

		#-----row1---
		fname=Label(frame,text="First Name",font=("times new roman ",15,"bold"),bg="white")
		fname.place(x=50,y=100)

		fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
		fname_entry.place(x=50,y=130,width=250)

		l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
		l_name.place(x=370,y=100)

		self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
		self.txt_lname.place(x=370,y=130,width=250)


		#=====row2=====
		contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
		contact.place(x=50,y=170)

		self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
		self.txt_contact.place(x=50,y=200,width=250)

		email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
		email.place(x=370,y=170)

		self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
		self.txt_email.place(x=370,y=200,width=250)

		#====row3=====
		security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
		security_Q.place(x=50,y=240)

		self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
		self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend Name","Your Favourite food")
		self.combo_security_Q.place(x=50,y=270,width=250)
		self.combo_security_Q.current(0)

		security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
		security_A.place(x=370,y=240)

		self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
		self.txt_security.place(x=370,y=270,width=250)


		#====row4=====
		pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
		pswd.place(x=50,y=310)

		self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
		self.txt_pswd.place(x=50,y=340,width=250)

		confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
		confirm_pswd.place(x=370,y=310)

		self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show="*")
		self.txt_confirm_pswd.place(x=370,y=340,width=250)

		#Check button
		self.var_check=IntVar()
		checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms & conditions", font=("times new roman",12,"bold"),onvalue=1, offvalue=0,bg="white")
		checkbtn.place(x=50,y=380)

		#=============Buttons============
		img=Image.open(r"D:\machine\img\RegR.jpg")
		img=img.resize((200,50),Image.ANTIALIAS)
		self.photoimage=ImageTk.PhotoImage(img)
		b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2")
		b1.place(x=10,y=420,width=200)

		#Login Button
		img1=Image.open(r"D:\machine\img\loginR.png")
		img1=img1.resize((200,50),Image.ANTIALIAS)
		self.photoimage1=ImageTk.PhotoImage(img1)
		b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
		b1.place(x=330,y=420,width=200)

	
	#=============Functions============

	#Register validation
	def register_data(self):
		if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
			messagebox.showerror("Error", "All fields are required",parent=self.root)
		elif self.var_pass.get()!=self.var_confpass.get():
			messagebox.showerror("Error", "Password & Confirm Password must be same",parent=self.root)
		elif self.var_check.get()==0:
			messagebox.showerror("Error", "Please agree our terms & conditions",parent=self.root)

		else:
			#Connecting with database
			conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")			
			my_cursor=conn.cursor()

			#for the unique email (1 email 1 user(not duplicate user with same mail))
			query=("select * from register where email=%s")
			value=(self.var_email.get(),)
			my_cursor.execute(query,value)

			#fetching data from db
			row=my_cursor.fetchone()
			if row!=None:
				messagebox.showerror("Error", "User already exists, please try another email",parent=self.root)
			else:
				my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

																						self.var_fname.get(),
																						self.var_lname.get(),
																						self.var_contact.get(),
																						self.var_email.get(),
																						self.var_securityQ.get(),
																						self.var_securityA.get(),
																						self.var_pass.get()
																					))		
			conn.commit()
			conn.close()
			messagebox.showinfo("Success", "Registered Successfully",parent=self.root)	



	#=====for login button from register page====
	
	def return_login(self):
		self.root.destroy()		

#=============Copied from Face recognition Sytem for login===========

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

	#Help desk button====
		img7=Image.open(r"D:\machine\img\help.jpg")
		
		img7=img7.resize((220,220),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.help_data)
		b1.place(x=1100,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_data,font=("Sketchy In Snow", 15,"bold"),bg="darkblue",fg="white")
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
	def help_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Help(self.new_window)		

if __name__=="__main__":
	main()
		
		
		