from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

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
        img3= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/dev.jpg")
        img3=img3.resize((screen_width,int(screen_height*(2/2.6))),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=(screen_height/3-100),width=screen_width,height=screen_height*(2/2.6))

        title_lb1=Label(bg_img,text="DEVELOPER (SHIVA TEJA)",font=("times new roman",35,"bold"),bg="SkyBlue",fg="navy")
        title_lb1.place(x=0,y=0,width=screen_width,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1235,y=-10,width=290,height=650)

        dev_label=Label(bg_img,text="Email: shivateja369@gmail.com",font=("times new roman",25,"bold"),bg="SkyBlue",fg="navy")
        dev_label.place(x=0,y=550,width=500,height=40)


        img_left= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/ShivaTeja.jpg")
        img_left=img_left.resize((287,640),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(main_frame,image=self.photoimg_left)
        f_lb1.place(x=0,y=0,width=287,height=640)

        



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()