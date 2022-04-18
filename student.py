from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recongnition System")

		#=====variables for data base======
		self.var_dep=StringVar()
		self.var_course=StringVar()
		self.var_year=StringVar()
		self.var_semester=StringVar()
		self.var_std_id=StringVar()
		self.var_std_name=StringVar()
		self.var_div=StringVar()
		self.var_reg=StringVar()
		self.var_gender=StringVar()
		self.var_dob=StringVar()
		self.var_email=StringVar()
		self.var_phone=StringVar()
		self.var_address=StringVar()
		self.var_teacher=StringVar()


		self.search_by=StringVar()
		self.search_txt=StringVar()

		#First image section======	
		img=Image.open(r"D:\machine\img\student.jpg")
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
		title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Sketchy In Snow", 35,"bold"),bg="darkgreen",fg="red")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		main_frame=Frame(bg_img,bd=2)
		main_frame.place(x=10,y=55,width=1500,height=600)

		#left frame label
		Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
		Left_frame.place(x=10,y=10,width=730,height=580)

		img_left=Image.open(r"D:\machine\img\stdnt.jpg")
		
		img_left=img_left.resize((720,130),Image.ANTIALIAS)
		self.photoimg_left=ImageTk.PhotoImage(img_left)

		f_lbl=Label(Left_frame,image=self.photoimg_left)
		f_lbl.place(x=5,y=0,width=720,height=130)

		#current course
		Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
		Current_course_frame.place(x=5,y=135,width=720,height=150)

		#department
		dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
		dep_label.grid(row=0,column=0,padx=10,sticky=W)

		dep_combo=ttk.Combobox(Current_course_frame, textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
		dep_combo["values"]=("Select Department","Computer Applications","Computer Science")
		dep_combo.current(0)
		dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		#course
		course_label=Label(Current_course_frame,text="Courses",font=("times new roman",12,"bold"),bg="white")
		course_label.grid(row=0,column=2,padx=10,sticky=W)

		course_combo=ttk.Combobox(Current_course_frame, textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
		course_combo["values"]=("Select Course","MCA","MSc")
		course_combo.current(0)
		course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

		#year
		year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
		year_label.grid(row=1,column=0,padx=10,sticky=W)

		year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
		year_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022")
		year_combo.current(0)
		year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

		#semester
		semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
		semester_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

		semester_combo=ttk.Combobox(Current_course_frame, textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
		semester_combo["values"]=("Select Semester","sem-I","sem-II","sem-III","sem-IV","sem-V","sem-VI")
		semester_combo.current(0)
		semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

		#class stduent Information
		Class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
		Class_student_frame.place(x=5,y=250,width=720,height=300)

		#student id label
		studentID_label=Label(Class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
		studentID_label.grid(row=0,column=0,padx=10,sticky=W)

		studentID_entry=ttk.Entry(Class_student_frame, textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
		studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

		#student name label
		studentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
		studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

		studentName_entry=ttk.Entry(Class_student_frame, textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
		studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

		#student divison label
		student_div_label=Label(Class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
		student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)		

		div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly", width=18)
		div_combo["values"]=("A","B","C")
		div_combo.current(0)
		div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

		#student Reg label
		studentReg_label=Label(Class_student_frame,text="Reg No:",font=("times new roman",12,"bold"),bg="white")
		studentReg_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

		studentReg_entry=ttk.Entry(Class_student_frame,  textvariable=self.var_reg,width=20,font=("times new roman",12,"bold"))
		studentReg_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

		#student gender label
		gender_label=Label(Class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
		gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
	
		gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly", width=18)
		gender_combo["values"]=("Male","Female","Other")
		gender_combo.current(0)
		gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

		#student DOB label
		dob_label=Label(Class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
		dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

		dob_entry=ttk.Entry(Class_student_frame, textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
		dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

		#student Email label
		email_label=Label(Class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
		email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

		email_entry=ttk.Entry(Class_student_frame, textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
		email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

		#student phone no label
		phone_label=Label(Class_student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white")
		phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

		phone_entry=ttk.Entry(Class_student_frame, textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
		phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

		#student address label
		address_label=Label(Class_student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
		address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

		address_entry=ttk.Entry(Class_student_frame, textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
		address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

		#teacher label
		teacher_label=Label(Class_student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
		teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

		teacher_entry=ttk.Entry(Class_student_frame, textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
		teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

		#radio buttons
		self.var_radio1=StringVar()
		radiobtn1=ttk.Radiobutton(Class_student_frame, variable=self.var_radio1,text="Take Photo Sample",value="Yes")
		radiobtn1.grid(row=6,column=0)

		#self.var_radio2=StringVar()
		radiobtn2=ttk.Radiobutton(Class_student_frame, variable=self.var_radio1,text="No Photo Sample",value="No")
		radiobtn2.grid(row=6,column=1)

		#buttons frame
		btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
		btn_frame.place(x=0,y=200,width=715,height=35)

		save_btn=Button(btn_frame,text="Save", command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="darkgreen",fg="red")
		save_btn.grid(row=0,column=0)

		update_btn=Button(btn_frame,text="Update", command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="darkgreen",fg="red")
		update_btn.grid(row=0,column=1)

		delete_btn=Button(btn_frame,text="Delete",command=self. delete_data,width=19,font=("times new roman",12,"bold"),bg="darkgreen",fg="red")
		delete_btn.grid(row=0,column=2)

		reset_btn=Button(btn_frame,text="Reset", command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="darkgreen",fg="red")
		reset_btn.grid(row=0,column=3)

		#for 2nd button frame 
		btn_frame1=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
		btn_frame1.place(x=0,y=235,width=715,height=35)

		take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=40,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
		take_photo_btn.grid(row=0,column=0)

		update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
		update_photo_btn.grid(row=0,column=1)

		#right frame label
		Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
		Right_frame.place(x=750,y=10,width=660,height=580)

		#image section
		img_right=Image.open(r"D:\machine\img\group cls 02.jpg")
		
		img_right=img_right.resize((720,130),Image.ANTIALIAS)
		self.photoimg_right=ImageTk.PhotoImage(img_right)

		f_lbl2=Label(Right_frame,image=self.photoimg_right)
		f_lbl2.place(x=5,y=0,width=720,height=130)

		#search system
		search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
		search_frame.place(x=5,y=135,width=650,height=70)

		search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="green",fg="white")
		search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

		search_combo=ttk.Combobox(search_frame,textvariable=self.search_by,font=("times new roman",12,"bold"),state="readonly",width=10)
		search_combo["values"]=("Select","reg","id")
		search_combo.current(0)
		search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		search_entry=ttk.Entry(search_frame,textvariable=self.search_txt,width=15,font=("times new roman",12,"bold"))
		search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


		search_btn=Button(search_frame,text="Search",width=12,command=self.search_data,font=("times new roman",12,"bold"),bg="green",fg="white")
		search_btn.grid(row=0,column=3,padx=4)

		showAll=Button(search_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",12,"bold"),bg="green",fg="white")
		showAll.grid(row=0,column=4,padx=4)

		#table frame

		table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
		table_frame.place(x=5,y=210,width=650,height=350)

		scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

		self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","reg","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.student_table.xview)
		scroll_y.config(command=self.student_table.yview)

		self.student_table.heading("dep",text="Department")
		self.student_table.heading("course",text="Course")
		self.student_table.heading("year",text="Year")
		self.student_table.heading("sem",text="Semester")
		self.student_table.heading("id",text="ID")
		self.student_table.heading("name",text="Name")
		self.student_table.heading("div",text="Division")
		self.student_table.heading("reg",text="Registration No")
		self.student_table.heading("gender",text="Gender")
		self.student_table.heading("dob",text="DOB")
		self.student_table.heading("email",text="Email")
		self.student_table.heading("phone",text="Phone")
		self.student_table.heading("address",text="Address")
		self.student_table.heading("teacher",text="Teacher")
		self.student_table.heading("photo",text="PhotoSampleStatus")
		self.student_table["show"]="headings"

		#========Width Setting======
		self.student_table.column("dep",width=100)
		self.student_table.column("course",width=100)
		self.student_table.column("year",width=100)
		self.student_table.column("sem",width=100)
		self.student_table.column("id",width=100)
		self.student_table.column("name",width=100)
		self.student_table.column("div",width=100)
		self.student_table.column("reg",width=100)
		self.student_table.column("gender",width=100)
		self.student_table.column("dob",width=100)
		self.student_table.column("email",width=100)
		self.student_table.column("phone",width=100)
		self.student_table.column("address",width=100)
		self.student_table.column("teacher",width=100)
		self.student_table.column("photo",width=100)

		self.student_table.pack(fill=BOTH,expand=1)
		self.student_table.bind("<ButtonRelease>",self.get_cursor)
		#function calling
		self.fetch_data()

	#====function declaration for query in db====
	
	def add_data(self):
		if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
			messagebox.showerror("Error","All fields are required",parent=self.root)
		else:
			try:
				#Connecting with database
				conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
					(


						self.var_dep.get(),
						self.var_course.get(),
						self.var_year.get(),
						self.var_semester.get(),
						self.var_std_id.get(),
						self.var_std_name.get(),
						self.var_div.get(),
						self.var_reg.get(),
						self.var_gender.get(),
						self.var_dob.get(),
						self.var_email.get(),
						self.var_phone.get(),
						self.var_address.get(),
						self.var_teacher.get(),
						self.var_radio1.get()
					))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Success","Student details has been added Successfully", parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)	

	#=====fetching data from database for shwoing on display board====
	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
		my_cursor=conn.cursor()
		my_cursor.execute("Select * from student ")
		data=my_cursor.fetchall()

		if len(data)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for i in data:
				self.student_table.insert("",END,values=i)
			conn.commit() #for keep updating data
		conn.close()	

	#===creating func for cursor focus to update data===

	def get_cursor(self,event=""):
		cursor_focus=self.student_table.focus()
		content=self.student_table.item(cursor_focus)
		data=content["values"]

		self.var_dep.set(data[0]),
		self.var_course.set(data[1]),
		self.var_year.set(data[2]),								
		self.var_semester.set(data[3]),
		self.var_std_id.set(data[4]),
		self.var_std_name.set(data[5]),
		self.var_div.set(data[6]),
		self.var_reg.set(data[7]),
		self.var_gender.set(data[8]),
		self.var_dob.set(data[9]),
		self.var_email.set(data[10]),
		self.var_phone.set(data[11]),
		self.var_address.set(data[12]),
		self.var_teacher.set(data[13]),
		self.var_radio1.set(data[14])

	#===update function====
	def update_data(self):
		if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
			messagebox.showerror("Error","All fields are required",parent=self.root)
		else:
			try:
				Update=messagebox.askyesno("Update","Do you wanna update this Student Details", parent=self.root)
				if Update > 0:
					conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
					my_cursor=conn.cursor()
					my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Reg=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
																														self.var_dep.get(),
																														self.var_course.get(),																																														
																														self.var_year.get(),
																														self.var_semester.get(),
																														self.var_std_name.get(),
																														self.var_div.get(),
																														self.var_reg.get(),
																														self.var_gender.get(),
																														self.var_dob.get(),
																														self.var_email.get(),
																														self.var_phone.get(),
																														self.var_address.get(),
																														self.var_teacher.get(),
																														self.var_radio1.get(),
																														self.var_std_id.get()
																														
																														
																													)) 
																														

																														

																													


																															

																													

				else:
					if not Update:
						return
				messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
				conn.commit()
				self.fetch_data()			
				conn.close()
								
			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

	#====delete function====
	
	def delete_data(self):
		if self.var_std_id.get()=="":
			messagebox.showerror("Error","Student Id must be required!", parent=self.root)
		else:
			try:
				delete=messagebox.askyesno("Heads Up!","Do you wanna delete this Student?",parent=self.root)							
				if delete:
					conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
					my_cursor=conn.cursor()
					sql="delete from student where Student_id=%s"
					val=(self.var_std_id.get(),)
					my_cursor.execute(sql,val)
				else:
					if not delete:
						return	

				conn.commit()
				self.fetch_data()			
				conn.close()		
				messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)	

	#Reset ffunction

	def reset_data(self):

		self.var_dep.set("Select Department")
		self.var_course.set("Select Course")
		self.var_year.set("Select Year")								
		self.var_semester.set("Select Semester")
		self.var_std_id.set("")
		self.var_std_name.set("")
		self.var_div.set("Select Division")
		self.var_reg.set("")
		self.var_gender.set("Male")
		self.var_dob.set("")
		self.var_email.set("")
		self.var_phone.set("")
		self.var_address.set("")
		self.var_teacher.set("")
		self.var_radio1.set("")
								
	#=====Generate Dataset and Take Photo Samples====
	
	def generate_dataset(self):
		if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
			messagebox.showerror("Error","All fields are required",parent=self.root)
		else:
			try:
				
				conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
				my_cursor=conn.cursor()
				my_cursor.execute("select * from student")
				myresult=my_cursor.fetchall()
				id=0
				for x in myresult:
					id+=1

				my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Reg=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
																														self.var_dep.get(),
																														self.var_course.get(),																																														
																														self.var_year.get(),
																														self.var_semester.get(),
																														self.var_std_name.get(),
																														self.var_div.get(),
																														self.var_reg.get(),
																														self.var_gender.get(),
																														self.var_dob.get(),
																														self.var_email.get(),
																														self.var_phone.get(),
																														self.var_address.get(),
																														self.var_teacher.get(),
																														self.var_radio1.get(),
																														self.var_std_id.get()==id+1
																														
																														
																													)) 
				conn.commit()
				self.fetch_data()
				self.reset_data()
				conn.close()

				#Load predefined data on face frontals from OpenCV
				face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

				def face_cropped(img):
					gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					faces=face_classifier.detectMultiScale(gray, 1.3, 5)
					#sacling factor by default=1.3
					#Min Neighbor=5

					for(x,y,w,h) in faces:
						face_cropped=img[y:y+h, x:x+w]
						return face_cropped

				#Opening camera
				cap=cv2.VideoCapture(0) # here 0 is the camera weight
				img_id=0
				while True:
					ret,my_frame=cap.read()
					if face_cropped (my_frame) is not None:
						img_id+=1
						face=cv2.resize(face_cropped(my_frame),(450,450))
						face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

						file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
						cv2.imwrite(file_name_path, face)
						cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
						cv2.imshow("Cropped Face", face)

					if cv2.waitKey(1)==13 or int(img_id)==100:
						break
				cap.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Result", "Generating data sets Completed!")
					
			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)	

	# Search by function
	def search_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
		my_cursor=conn.cursor()
		my_cursor.execute("Select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END, values=row)
			conn.commit()	
		conn.close()			
		


																																																			
if __name__=="__main__":
	root=Tk()
	obj=Student(root)
	root.mainloop()	
		