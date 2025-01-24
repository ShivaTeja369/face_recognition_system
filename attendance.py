from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #=======variables(to get data in entry from table)=======
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



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

        title_lb1=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="yellow")
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
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=5,width=screen_width/2,height=584)

        img_left= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/AdobeStock_303989091.jpeg")
        img_left=img_left.resize((int(screen_width/2),180),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=0,y=0,width=screen_width/2,height=180)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=180,width=screen_width,height=400)

        #Labels and entries
        #attendence id
        attendanceId_label=Label(left_inside_frame,text="AttendenceID:",font=("times new roman",15,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",15,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        rollId_label=Label(left_inside_frame,text="Roll:",font=("times new roman",15,"bold"),bg="white")
        rollId_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        rollID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",15,"bold"))
        rollID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",15,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",15,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        dep_label=Label(left_inside_frame,text="Time:",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",15,"bold"))
        dep_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        dep_label=Label(left_inside_frame,text="Date:",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",15,"bold"))
        dep_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendence Status
        dep_label=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        # dep_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",15,"bold"))
        # dep_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(left_inside_frame,font=("times new roman",15,"bold"),width=18,textvariable=self.var_atten_attendance,state="read only")
        div_combo["values"]=("Status","Present","Absent")
        div_combo.current(0)
        div_combo.grid(row=3,column=1,padx=9,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=310,width=screen_width/2,height=45)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=screen_width/2,y=0,width=screen_width/2,height=screen_height*(5/6)-50)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=screen_width/2-15,height=screen_height*(5/6)-195)

# ===============Scroll bar table===============
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"  #to remove empty space in 1st column of headings

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)


        self.AttendenceReportTable.pack(fill=BOTH, expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #============fetch data==================
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

   #=====import csv============ 
    def importCsv(self):
        global mydata
        mydata.clear() #to clear the previously opened data if present
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"), ("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #=====export csv==============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"), ("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to {str(es)}",parent= self.root) 
                    
     #======get cursor=============
    def get_cursor(self,event=''):
        cursor_row=self.AttendenceReportTable.focus()  
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        
        self.var_atten_id.set(rows[0]) 
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6])    

    
    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendance.set("")    








if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()       