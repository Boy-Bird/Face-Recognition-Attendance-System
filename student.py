from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ============variables=============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_sec = StringVar()
        self.var_fathername = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phoneno = StringVar()
        self.var_address = StringVar()
        self.var_teachername = StringVar()


        # first image
        img = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        # second image
        img1 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

        # third image
        img2 = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\GEHU.jpg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)

        title_lbl = Label(self.root, text='STUDENT MANAGEMENT SYSTEM', font=('times new roman', 35, 'bold'),
                          bg='white', fg='black')
        title_lbl.place(x=0,y=150,width=1530,height=40)

        main_frame=Frame(self.root,bd=2, )
        main_frame.place(x=0,y=200,width=1500,height=600)

        # left Label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\bluebg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Details",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # dep_label = Label(current_course_frame,text='Department',font=("times new roman",12,"bold"))
        # dep_label.grid(row=0,column=0,padx=3)
        #
        # dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state='readonly')
        # dep_combo['values']=('Select Department','Computer','IT','Civil','Mechanical')
        # dep_combo.current(0)
        # dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="pink")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 13),state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "Mechanical Engineering", "Civil Engineering", "IT", "Specialization")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12),state="readonly", width=20)
        course_combo["values"] = ("Select Course", "B.Tech", "B.Sc", "B.Com", "BCA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 13), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman", 12),state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        # Class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student information",font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        #student id
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"))
        studentId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student's name
        studentName_label = Label(class_Student_frame, text="Student's Name:", font=("times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman", 13,"bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll no
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"))
        roll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_rollno,width=20,font=("times new roman", 13,'bold'))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Section
        sec_label = Label(class_Student_frame, text="Section:", font=("times new roman", 13, "bold"),fg="black")
        sec_label.grid(row=1, column=2, padx=10, sticky=W)

        sec_entry = ttk.Entry(class_Student_frame,textvariable=self.var_sec, width=20, font=("times new roman", 13))
        sec_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Father's Name
        father_label = Label(class_Student_frame, text="Father's Name:", font=("times new roman", 13, "bold"))
        father_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        father_entry = ttk.Entry(class_Student_frame,textvariable=self.var_fathername, width=20,font=("times new roman", 13))
        father_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20,font=("times new roman", 13))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phoneno, width=20,font=("times new roman", 13))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20,font=("times new roman", 13))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher's Name:", font=("times new roman", 13, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teachername, width=20,font=("times new roman", 13))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text='take photo sample',value='Yes')
        radionbtn1.grid(row=6,column=0)


        radionbtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text='no photo sample', value='No')
        radionbtn2.grid(row=6, column=1)

        # button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=19,font=("times new roman", 13),bg='black',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text='Update',command=self.update_data, width=19, font=("times new roman", 13), bg='black', fg='white')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Delete',command=self.delete_data, width=19, font=("times new roman", 13), bg='black', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data, width=19, font=("times new roman", 13), bg='black', fg='white')
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1,command = self.generate_dataset, text='Take Photo Sample', width=39, font=("times new roman", 13), bg='red', fg='white')
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text='Update Photo Sample', width=39, font=("times new roman", 13), bg='black',fg='white')
        update_photo_btn.grid(row=0, column=1)





        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Users\yashp\OneDrive\Documents\FaceRecog\images\bluebg.png")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ==========Search System============
        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System",font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame,text="Search By:", font=("times new roman", 15, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12), state="readonly", width=15)
        search_combo["values"] = ("Select ", "Roll_no", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=19, font=("times new roman", 11))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text='Search', width=14, font=("times new roman", 11), bg='black', fg='white')
        search_btn.grid(row=0, column=3,padx=4)

        showAll_btn = Button(Search_frame, text='Show All', width=14, font=("times new roman", 11), bg='black', fg='white')
        showAll_btn.grid(row=0, column=4,padx=4)


        # =============table frame=============
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep","course", "year", "sem", "id", "name", "roll", "sec", "father", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student's ID")
        self.student_table.heading("name",text="Student's Name")
        self.student_table.heading("roll", text="University RollNo")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("father", text="Father's Name")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher's Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"


        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("father", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=160)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # =================function declaration===========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="6666",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_sec.get(),
                    self.var_fathername.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phoneno.get(),
                    self.var_address.get(),
                    self.var_teachername.get(),
                    self.var_radio1.get()


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)

    # ================fetch data===========
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="6666", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============get cursor==========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_rollno.set(data[6]),
        self.var_sec.set(data[7]),
        self.var_fathername.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phoneno.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teachername.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):

        if self.var_dep.get() == "Select Department" or self.var_name == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update Student's Information", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="6666", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Section=%s,FathersName=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,TeachersName=%s, PhotoSample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_rollno.get(),
                            self.var_sec.get(),
                            self.var_fathername.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phoneno.get(),
                            self.var_address.get(),
                            self.var_teachername.get(),
                            self.var_radio1.get(),
                            self.var_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success!!", "Details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    #=============Delete Function================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error!","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="6666",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #=============Reset===========
    def reset_data(self):
        self.var_name.set("")
        self.var_id.set("")
        self.var_rollno.set("")
        self.var_fathername.set("")
        self.var_sec.set("")
        self.var_course.set("Select Course")
        self.var_dep.set("Select Branch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_teachername.set("")
        self.var_rollno.set("")
        self.var_radio1.set("")


    # ================== Generate data set or Take photo Samples ===========
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="6666", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Section=%s,FathersName=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,TeachersName=%s, PhotoSample=%s where Student_id=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_sec.get(),
                    self.var_fathername.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phoneno.get(),
                    self.var_address.get(),
                    self.var_teachername.get(),
                    self.var_radio1.get(),
                    self.var_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                 # ============= Load Predifined data on face frontals from opencv========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #sacaling factor = 1.3
                    #Minimum Neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450)) #,fx=100,fy=50)
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        # cv2.imshow('Video',my_frame)
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


