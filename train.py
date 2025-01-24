from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
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
        img3= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/wp2551980.jpg")
        img3=img3.resize((screen_width,int(screen_height*(2/2.6))),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=(screen_height/3-100),width=screen_width,height=screen_height*(2/2.6))

        title_lb1=Label(bg_img,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=screen_width,height=50)

        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",27,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=440,y=362,width=640,height=70)

    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img, 'uint8')
            id= int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        

        #==============Train the classifier and Save========
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
    


# print(cv2.__version__)
# print(help(cv2.face))



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()