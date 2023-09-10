import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help_desk import Help_desk
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        # second image
        img1 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img1 = img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        # third image
        img2 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)

        title_lbl = Label(self.root,text='FACE RECOGNITION ATTENDANCE SYSTEM',font=('times new roman',35,'bold'),bg='black',fg='white')
        title_lbl.place(x=0,y=150,width=1530,height=40)

        # student button
        img4 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\ad.png")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=120,y=225,width=200,height=200)

        b1_1 = Button(self.root,text='Student Deatils',command=self.student_details,cursor='hand2',font=('times new roman',15,'bold'),bg='white',fg='black')
        b1_1.place(x=120,y=422, width=200, height=40)

        # detect button
        img5 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\face_detection.jfif")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root, image=self.photoimg5, cursor='hand2',command=self.face_data)
        b1.place(x=455, y=225, width=200, height=200)

        b1_1 = Button(self.root, text='FaceDetector',command=self.face_data, cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=455, y=422, width=200, height=40)

        # Attendance
        img6 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\atten.png")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(self.root, image=self.photoimg6,command=self.attendance_data, cursor='hand2')
        b1.place(x=785, y=225, width=200, height=200)

        b1_1 = Button(self.root, text='Attendance', cursor='hand2',command=self.attendance_data, font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=785, y=422, width=200, height=40)

        # Help
        img7 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\help.png")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(self.root, image=self.photoimg7, cursor='hand2',command = self.help_desk)
        b1.place(x=1115,y=225, width=200, height=200)

        b1_1 = Button(self.root, text='Help', cursor='hand2',command = self.help_desk, font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=1115,y=422,width=200,height=40)

        # Train
        img8 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\train.jfif")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(self.root, image=self.photoimg8,command = self.train_data, cursor='hand2')
        b1.place(x=120,y=510,width=200, height=200)

        b1_1 = Button(self.root, text='Train Data',command = self.train_data, cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=120,y=707,width=200, height=40)

        # Photos
        img9 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\photos.png")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(self.root, image=self.photoimg9, cursor='hand2',command=self.open_img)
        b1.place(x=455, y=510, width=200, height=200)

        b1_1 = Button(self.root, text='Photos',command=self.open_img, cursor='hand2', font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=455, y=707, width=200, height=40)

        # Developer
        img10 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\dev.png")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(self.root, image=self.photoimg10, cursor='hand2',command = self.developer_data)
        b1.place(x=785,y=510, width=200, height=200)

        b1_1 = Button(self.root,text='Developer',cursor='hand2',command = self.developer_data, font=('times new roman', 15, 'bold'),
                      bg='white',fg='black')
        b1_1.place(x=785,y=707,width=200,height=40)

        # Exit
        img11 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\exit.png")
        img11 = img11.resize((200, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(self.root, image=self.photoimg11,command = self.exit, cursor='hand2')
        b1.place(x=1115, y=510, width=200, height=200)

        b1_1 = Button(self.root, text='Exit', cursor='hand2',command = self.exit, font=('times new roman', 15, 'bold'),
                      bg='white', fg='black')
        b1_1.place(x=1115, y=707, width=200, height=40)

    def open_img(self):
        os.startfile("data")


    # =============Functions buttons===============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_desk(self.new_window)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()