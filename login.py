import time
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\wallp.jpg")
        lbl_bg = Label(self.root,image = self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\add.png")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str = Label(frame,text="Get Started",font=("times new roman",20,'bold'),fg='white',bg='black')
        get_str.place(x=95,y=100)

        #label
        username=lbl = Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # ==========Icon Images =============
        img2 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\ad.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg='black', borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\lock1.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg='black', borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # Login Button
        loginbtn = Button(frame,text='Login',command = self.login,font=("times new roman", 15, "bold"),bd=3,relief=GROOVE,fg='orange',bg='black',activeforeground='orange',activebackground='black')
        loginbtn.place(x=110,y=307,width=120,height=35)

        # registerbutton
        registerbtn = Button(frame,text="New User Register",font=("times new roman",10,'bold'),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        registerbtn.place(x=15,y=370,width=160)

        # forget password button
        loginbtn = Button(frame, text='Forget Password', font=("times new roman", 10, "bold"),borderwidth=0,fg='white', bg='black', activeforeground='white', activebackground='black')
        loginbtn.place(x=10, y=390, width=160)

        # exit
        exit = Button(frame, text="Exit",command=self.exit, font=("times new roman", 10, 'bold'), borderwidth=0,
                             fg='white', bg='black', activeforeground='white', activebackground='black')
        exit.place(x=264, y=400, width=60)

    def login(self):
        if self.txtuser.get() == "admin" and self.txtpass.get()=="2356":
            messagebox.showinfo("Success","Welcome to Attendance System")
            self.proj()
            # time.sleep(5)
            # self.root.quit()
        else:
            messagebox.showinfo("Invalid","Invalid username or password")

    def proj(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    # def exitt(self):
    #     self.app=Face_Recognition_System()

    def exit(self):
        # self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent = self.root)
        # if self.exit > 0:
        self.root.destroy()
        # else:
        #     return


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()