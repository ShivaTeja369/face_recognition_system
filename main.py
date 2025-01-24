from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import tkinter
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")
        #self.root.geometry("1920x1080+0+0")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()


        #first img
        img= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/BestFacialRecognition.jpg")
        img=img.resize((int(screen_width/3),int(screen_height/4)),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=-50,width=int(screen_width/3),height=int(screen_height/3))

        #sec img
        img1= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/facialrecognition.png")
        img1 = img1.resize((int(screen_width/3), int(screen_height/4)), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=(screen_width/3),y=-50,width=(screen_width/3),height=(screen_height/3))

        
        #3rd img
        img2= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/images.jpg")
        img2=img2.resize((int(screen_width/3),int(screen_height/4)),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=2*(screen_width/3),y=-50,width=(screen_width/3),height=(screen_height/3))

        #background img
        img3= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/wp2551980.jpg")
        img3=img3.resize((screen_width,int(screen_height*(2/2.6))),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=(screen_height/3-100),width=screen_width,height=screen_height*(2/2.6))

        title_lb1=Label(bg_img,text="         FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=screen_width,height=50)

        #==========time====================
        def time():
            string = strftime('%H:%M:%S')
            lb1.config(text= string)
            lb1.after(1000, time)

        lb1 = Label(title_lb1, font=("times new roman",30,"bold"),bg="white",fg="blue")
        lb1.place(x=0,y=0,width=150,height=50)
        time()


        #student button
        img4= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/gettyimages-1022573162.jpg")
        img4=img4.resize((240,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=140,y=80,width=240,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=140,y=262,width=240,height=35)
        

        #Detect face button
        img5= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face_detector1.jpg")
        img5=img5.resize((240,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=480,y=80,width=240,height=220)

        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=480,y=262,width=240,height=35)


        #Attendance face button
        img6= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/IMG_1183_augmented_reality_faces1.jpg")    
        img6=img6.resize((240,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=820,y=80,width=240,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=820,y=262,width=240,height=35)


        #Help face button
        img7= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((240,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1160,y=80,width=240,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1160,y=262,width=240,height=35)


        #Train face button
        img8= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/Train.jpg")
        img8=img8.resize((240,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=140,y=340,width=240,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=140,y=524,width=240,height=35)


        #Photos face button
        img9= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/opencv_face_reco_more_data.jpg")
        img9=img9.resize((240,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=480,y=340,width=240,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=480,y=524,width=240,height=35)


        #developer face button
        img10= Image.open("college_images/kisspng-website-wireframe-face-facial-recognition-system-w-recognition-5acafff32d2084.1500702215232532351849.jpg")
        img10=img10.resize((240,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=820,y=340,width=240,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=820,y=524,width=240,height=35)


        #exit face button
        img11= Image.open("college_images/exit.jpg")
        img11=img11.resize((240,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1160,y=340,width=240,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1160,y=524,width=240,height=35)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

   #====================Functions buttons===============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Developer(self.new_window)

    





        

        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop() 

