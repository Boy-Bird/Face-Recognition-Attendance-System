from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text='Face Recognition', font=('times new roman', 35, 'bold'), bg='white',
                          fg='blue')
        title_lbl.place(x=0, y=0, width=1530, height=70)

        # img = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\bg.jpg")
        # img = img.resize((1250,900), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)
        #
        # bg_img = Label(self.root,image=self.photoimg)
        # bg_img.place(x=125,y=175,width=1250,height=550)

        b1_1 = Button(self.root, text='Face Recognition',command=self.face_recog,  cursor='hand2',
                      font=('times new roman', 35, 'bold'), bg='white', fg='black')
        b1_1.place(x=570, y=380, width=420, height=40)

    def attendance(self, i, r, n, d):
        # print(r)
        with open("Atten.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            # print(name_list)
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            # print(name_list)
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
             # ((r not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt},{d1},Present")


    # =============Face Recognition=============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id,predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="6666", database="face_recognizer")
                my_cursor = conn.cursor()
                #
                #
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                # i = str(i).strip('(,)')
                i = "+".join(i)
                #
                my_cursor.execute("select RollNo from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                # r = str(r).strip('(,)')
                r = "+".join(r)
                #
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                # n = str(n).strip('(,)')
                n = "+".join(n)
                #
                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                # d = str(d).strip(',()')
                d = "+".join(d)

                if confidence > 77:
                    # cv2.putText(img, f'Id:{i}', (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    cv2.putText(img, f"Roll:{r}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dep:{d}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.attendance(i, r, n, d)
                    # cv2.putText(img,'Yash Parihar',(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y -20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]


            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognizer", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()