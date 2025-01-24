from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        
        #first img
        img= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/BestFacialRecognition.jpg")
        img=img.resize((700,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=700,height=200)

        
        #sec img
        img1= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/facialrecognition.png")
        img1=img1.resize((740,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=600,y=0,width=740,height=200)

        
        #3rd img
        img2= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/images.jpg")
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

        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1920,height=50)

        #student button
        img4= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/gettyimages-1022573162.jpg")
        img4=img4.resize((240,240),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=240,y=100,width=240,height=240)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=240,y=320,width=240,height=50)
        

        #Detect face button
        img5= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face_detector1.jpg")
        img5=img5.resize((240,240),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=580,y=100,width=240,height=240)

        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=580,y=320,width=240,height=50)


        #Attendance face button
        img6= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/IMG_1183_augmented_reality_faces1.jpg")    
        img6=img6.resize((240,240),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=920,y=100,width=240,height=240)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=920,y=320,width=240,height=50)


        #Help face button
        img7= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((240,240),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1260,y=100,width=240,height=240)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1260,y=320,width=240,height=50)


        #Train face button
        img8= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/Train.jpg")
        img8=img8.resize((240,240),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=240,y=400,width=240,height=240)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=240,y=620,width=240,height=50)


        #Photos face button
        img9= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/opencv_face_reco_more_data.jpg")
        img9=img9.resize((240,240),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=580,y=400,width=240,height=240)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=580,y=620,width=240,height=50)


        #developer face button
        img10= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/kisspng-website-wireframe-face-facial-recognition-system-w-recognition-5acafff32d2084.1500702215232532351849.jpg")
        img10=img10.resize((240,240),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=920,y=400,width=240,height=240)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=920,y=620,width=240,height=50)


        #exit face button
        img11= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/exit.jpg")
        img11=img11.resize((240,240),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1260,y=400,width=240,height=240)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1260,y=620,width=240,height=50)

        

        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()