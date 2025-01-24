from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        title_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="darkblue",fg="yellow")
        title_lb1.place(x=0,y=0,width=screen_width,height=50)

        #first img
        img= Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face_detector1.jpg")
        img=img.resize((int(screen_width/2),int(screen_height*0.859)),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=50,width=int(screen_width/2),height=int(screen_height*0.859))

        #sec img
        img1= Image.open(r"C:\Users\Shiva\Desktop\FACE_RECOGNITION SYSTEM\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img1 = img1.resize((int(screen_width/2), int(screen_height*0.859)), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=(screen_width/2),y=50,width=(screen_width/2),height=(screen_height*0.859))

        b1_1=Button(f_lb1,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=210,y=662,width=340,height=35)


#===============attendance==============
    def mark_attendance(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")






#===============face recognition=================

    def face_recog(self):
        # def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        #     gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        #     coord=[]

        #     for (x,y,w,h) in features:
        #         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #         id,predict=clf.predict(gray_image[y:y+h,x:x+w])
        #         confidence=int((100*(1-predict/300)))

        #         conn=mysql.connector.connect(host="localhost",username="root",password="Shiva@mysql123",database="face recognizer")
        #         my_cursor = conn.cursor()

        #         my_cursor.execute("select Name from student where Student_id="+str(id))
        #         n=my_cursor.fetchone()
        #         n="+".join(n)

        #         my_cursor.execute("select Roll from student where Student_id="+str(id))
        #         r=my_cursor.fetchone()
        #         r="+".join(r)

        #         my_cursor.execute("select dep from student where Student_id="+str(id))
        #         d=my_cursor.fetchone()
        #         d="+".join(d)

        #         my_cursor.execute("select Student_id from student where Student_id="+str(id))
        #         i=my_cursor.fetchone()
        #         i="+".join(i)


        #         if confidence>77:
        #             cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Departmrnt:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             self.mark_attendance(i,r,n,d)
        #         else:
        #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        #             cv2.putText(img,"He's Dead! Who are you?",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

        #         coord=[x,y,w,h]

        #     return coord

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Shiva@mysql123", database="face recognizer")
                my_cursor = conn.cursor()

                # Fetch student details from database
                my_cursor.execute("select Name from student where Student_id=%s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("select Roll from student where Student_id=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("select dep from student where Student_id=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id=%s", (id,))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        # while True:
        #     ret,img=video_cap.read()
        #     img=recognize(img,clf,faceCascade)
        #     cv2.imshow("Welcome to Face Recognition",img)

        #     if cv2.waitKey(1)==13:
        #         break
        # video_cap.release()
        # cv2.destroyAllWindows()

        try:
            while True:
                ret, img = video_cap.read()
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Press Enter to exit
                    print("Exiting Face Recognition.")
                    break
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected. Closing...")
        finally:
            video_cap.release()
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()       










# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import cv2
# import os
# import numpy as np


# class Face_recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Face Recognition System")

#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()

#         title_lb1 = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="darkblue", fg="yellow")
#         title_lb1.place(x=0, y=0, width=screen_width, height=50)

#         # First image
#         img = Image.open("/users/shiva/Desktop/FACE_RECOGNITION SYSTEM/college_images/face_detector1.jpg")
#         img = img.resize((int(screen_width / 2), int(screen_height * 0.859)), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)

#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=50, width=int(screen_width / 2), height=int(screen_height * 0.859))

#         # Second image
#         img1 = Image.open(
#             r"C:\Users\Shiva\Desktop\FACE_RECOGNITION SYSTEM\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
#         img1 = img1.resize((int(screen_width / 2), int(screen_height * 0.859)), Image.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         f_lb1 = Label(self.root, image=self.photoimg1)
#         f_lb1.place(x=(screen_width / 2), y=50, width=(screen_width / 2), height=(screen_height * 0.859))

#         b1_1 = Button(f_lb1, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 20, "bold"), bg="red", fg="white")
#         b1_1.place(x=210, y=662, width=340, height=35)

#     # Mark attendance
#     def mark_attendance(self, i, r, n, d):
#         try:
#             # Open the file in append mode to create it if it doesn't exist
#             with open("attendance.csv", "a+", newline="\n") as f:
#                 f.seek(0)  # Go to the beginning of the file
#                 myDataList = f.readlines()
#                 name_list = [line.split(",")[0] for line in myDataList]

#                 # Check if attendance for this ID already exists
#                 if i not in name_list:
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")
#                     f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
#         except Exception as e:
#             print(f"Error in mark_attendance: {e}")


#     # Face recognition
#     def face_recog(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

#             coord = []

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#                 confidence = int((100 * (1 - predict / 300)))

#                 conn = mysql.connector.connect(host="localhost", username="root", password="Shiva@mysql123", database="face recognizer")
#                 my_cursor = conn.cursor()

#                 try:
#                     # Fetch Name
#                     my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
#                     n = my_cursor.fetchone()
#                     n = n[0] if n else "Unknown"  # Assign "Unknown" if fetchone() returns None

#                     # Fetch Roll
#                     my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
#                     r = my_cursor.fetchone()
#                     r = r[0] if r else "Unknown"

#                     # Fetch Department
#                     my_cursor.execute("SELECT dep FROM student WHERE Student_id = %s", (id,))
#                     d = my_cursor.fetchone()
#                     d = d[0] if d else "Unknown"

#                     # Fetch Student ID
#                     my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (id,))
#                     i = my_cursor.fetchone()
#                     i = i[0] if i else "Unknown"

#                 except Exception as e:
#                     print(f"Database error: {e}")
#                     n, r, d, i = "Unknown", "Unknown", "Unknown", "Unknown"

#                 # Display details if confidence is high enough
#                 if confidence > 77:
#                     cv2.putText(img, f"ID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     self.mark_attendance(i, r, n, d)
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Person", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

#                 coord = [x, y, w, h]

#             return coord





#         def recognize(img, clf, faceCascade):
#             coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
#             return img

#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap = cv2.VideoCapture(0)

#         while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Welcome to Face Recognition", img)

#             if cv2.waitKey(1) == 13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()
