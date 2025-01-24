from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()     

      #=================variables(to show data on entry by cliking on table in website)=====
        
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
  

        #first img
        img= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face-recognition.png")
        img=img.resize((int(screen_width/3),int(screen_height/6)),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=int(screen_width/3),height=int(screen_height/6))

        #sec img
        img1= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/smart-attendance.jpg")
        img1=img1.resize((int(screen_width/3),int(screen_height/6)),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=(screen_width/3),y=0,width=int(screen_width/3),height=int(screen_height/6 ))
       
        #3rd img
        img2= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/iStock-182059956_18390_t12.jpg")
        img2=img2.resize((int(screen_width/3),int(screen_height/6)),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=2*(screen_width/3),y=0,width=int(screen_width/3),height=int(screen_height/6))

        #background img
        img3= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/wp2551980.jpg")
        img3=img3.resize((1920,880),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=screen_height/6,width=screen_width,height=screen_height*(5/6))

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=-150,y=0,width=1920,height=50)

        #==========time====================
        def time():
            string = strftime('%H:%M:%S')
            lb1.config(text= string)
            lb1.after(1000, time)

        lb1 = Label(title_lb1, font=("times new roman",30,"bold"),bg="black",fg="yellow")
        lb1.place(x=150,y=0,width=150,height=50)
        time()

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=screen_width,height=800)

        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=5,width=screen_width/2,height=680)

        img_left= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/AdobeStock_303989091.jpeg")
        img_left=img_left.resize((int(screen_width/2),180),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=0,y=0,width=screen_width/2,height=180)


        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",15,"bold"))
        current_course_frame.place(x=0,y=130,width=940,height=130)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","BE","FE","SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),width=17,state="read only")
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",15,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",15,"bold"))
        class_Student_frame.place(x=0,y=260,width=940,height=300)


        #student id
        student_Id_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",15,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",15,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",15,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",15,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",15,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),width=18,state="read only")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=9,pady=10,sticky=W)

        #roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",15,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",15,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),width=18,state="read only")
        gender_combo["values"]=("Male","Female","Agender","Bigender","Transgender","Trigender","None")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=9,pady=10,sticky=W)


        #dob
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",15,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",15,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",15,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=0,pady=0)

    
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=0,pady=0)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=screen_width/2,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame1
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=920,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",15,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=screen_width/2,y=0,width=screen_width/2,height=screen_width*(5/6)-50)

        img_right= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/gettyimages-1022573162.jpg")
        img_right=img_right.resize((950,140),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=950,height=140)

        # ============Search System================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        Search_frame.place(x=10,y=140,width=740,height=80)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",15,"bold"),width=10,state="read only")
        search_combo["values"]=("Select","Roll-No","Phonr-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=25,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="showAll",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #=============table frame===========
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=740,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year", text="Year") 
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId") 
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No") 
        self.student_table.heading("gender", text="Genders")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")   
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address") 
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus") 
        self.student_table["show"]="headings"
        

                
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100) 
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #======================Function declaraton(add data into mysql table)================= 

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
                my_cursor = conn.cursor()   
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                          
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(), 
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(), 
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(), 
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
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
                # my_cursor.close()
                messagebox.showinfo("Hurray!", "Student details saved succesfully",parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent= self.root) 
            
    
#============Fetch data from database to student table in website==============

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#==========get cursor(to show data on entry by cliking on table in website)================
    def get_cursor(self,event=""):  
        cursor_focus=self.student_table.focus() 
        content=self.student_table.item(cursor_focus)
        data=content ["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#============Update func (to update details by clicking on it)=============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                updatee= messagebox.askyesno("Update","Are you sure want to update the details",parent=self.root)
                if updatee>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s ", (
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(), 
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),                 
                                                                                                                                                                                                                                    self.var_std_name.get(), 
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                                      )) 
                    messagebox.showinfo("Hurray!", "Updated details successfully", parent= self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()  
                else:
                    if not updatee:
                        return
                
                
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}",parent=self.root)


#==========delete function===========

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is must",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("Delete","Successfully deleted students details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}",parent=self.root)

#====reset==========
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#========== Generate data set or take photosamples============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult= my_cursor.fetchall()  #storing all details from table in myresult
                # id=0
                # for x in myresult:
                #     id+=1     
                my_cursor.execute("update student set dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s ", (
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(), 
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),                 
                                                                                                                                                                                                                                    self.var_std_name.get(), 
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                                      )) 
                conn.commit()
                self.fetch_data()
                self.reset_data
                conn.close

                #========Load predefined data on face frontals from opencv=======

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame= cap.read()
                    
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face= cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path= f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)#font,font_scale,colour,thickness
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!! ")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}",parent=self.root)

            
                



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()