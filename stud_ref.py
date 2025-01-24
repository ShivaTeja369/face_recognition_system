from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        #first img
        img= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face-recognition.png")
        img=img.resize((700,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=700,height=200)

        #sec img
        img1= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/smart-attendance.jpg")
        img1=img1.resize((740,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=600,y=0,width=740,height=200)
       
        #3rd img
        img2= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/iStock-182059956_18390_t12.jpg")
        img2=img2.resize((580,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1340,y=0,width=580,height=200)

        #background img
        img3= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/wp2551980.jpg")
        img3=img3.resize((1920,880),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1920,height=880)

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1920,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1900,height=800)

        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=960,height=680)

        img_left= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/AdobeStock_303989091.jpeg")
        img_left=img_left.resize((950,180),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=950,height=200)


        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",15,"bold"))
        current_course_frame.place(x=10,y=200,width=940,height=130)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","BE","FE","SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",15,"bold"))
        class_Student_frame.place(x=10,y=340,width=940,height=300)


        #student id
        student_Id_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",15,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",15,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_Student_frame,text="No photo sample",value="Yes")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=920,height=30)

        save_btn=Button(btn_frame,text="Save",width=20,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=20,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=20,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame1
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=920,height=30)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=40,font=("times new roman",15,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=980,y=10,width=900,height=680)

        img_right= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/gettyimages-1022573162.jpg")
        img_right=img_right.resize((950,200),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=950,height=200)

        # ============Search System================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        Search_frame.place(x=10,y=210,width=880,height=80)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        search_combo["values"]=("Select","Roll-No","Phonr-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="showAll",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #=============table frame===========
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=300,width=880,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")




 



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()