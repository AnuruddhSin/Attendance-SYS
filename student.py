from tkinter import *
from tkinter import ttk

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")

        self.root.title("Face Recognition System")

        # ------------------ variables --------------------#

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First Image
        img = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\lu2.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\face-recognition-system-concept-human-260nw-1139961602.webp")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\lu.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl3 = Label(self.root, image=self.photoimg2)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # bG iMAGE

        img3 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lb1 = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman ", 35, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="gray")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left Label Frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="gray", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\student.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=720, height=120)

        # Current Course Label Frame

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        # Department Box

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=17)
        dep_combo["values"] = ("Select Department", "CSE", "CSE(Ai)", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=1, pady=10, sticky=W)

        # Courses Box
        courses_label = Label(current_course_frame, text="Courses", font=("times new roman", 12, "bold"))
        courses_label.grid(row=0, column=2, padx=10, sticky=W)

        courses_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                     font=("times new roman", 12, "bold"), width=17)
        courses_combo["values"] = ("Select Course", "CSE", "CSE(Ai)", "EE", "Civil", "ME")
        courses_combo.current(0)
        courses_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year Box
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=17)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester Box
        sem_label = Label(current_course_frame, text="Semester",
                          font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17)
        sem_combo["values"] = (
        "Select Semester", "Semester-I", "Semester-II", "Semester-III", "Semester-IV", "Semester-V", "Semester-VI",
        "Semester-VII", "Semester-VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=22, pady=10, sticky=W)

        # Class Student Label Frame

        class_student_info_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                              text="Class Student Information",
                                              font=("times new roman", 12, "bold"))
        class_student_info_frame.place(x=5, y=250, width=720, height=300)

        # Student Id

        studentId_label = Label(class_student_info_frame, text="StudentId:", font=("times new roman", 13, "bold"),
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_std_id, width=20,
                                    font=("times new roman ", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name

        studentName_label = Label(class_student_info_frame, text="Student Name:", font=("times new roman", 13, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_std_name, width=20,
                                      font=("times new roman ", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division

        classDiv_label = Label(class_student_info_frame, text="Class Division:", font=("times new roman", 13, "bold"),
                               bg="white")
        classDiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # classDiv_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_div, width=20,
        #                            font=("times new roman ", 13, "bold"))
        # classDiv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        classdiv_combo = ttk.Combobox(class_student_info_frame, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"), width=17)
        classdiv_combo["values"] = ("Select Division", "O", "A", "B","C","D","E","F")
        classdiv_combo.current(0)
        classdiv_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll Number

        rollNo_label = Label(class_student_info_frame, text="Roll No:", font=("times new roman", 13, "bold"),
                             bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_roll, width=20,
                                 font=("times new roman ", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender

        gender_label = Label(class_student_info_frame, text="Gender:", font=("times new roman", 13, "bold"),
                             bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # gender_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_gender, width=20,
        #                          font=("times new roman ", 13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_info_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), width=17)
        gender_combo["values"] = ("Select Gender", "Mail", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # DOB

        dob_label = Label(class_student_info_frame, text="DOB:", font=("times new roman", 13, "bold"),
                          bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman ", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email Id

        email_label = Label(class_student_info_frame, text="Email:",
                            font=("times new roman", 13, "bold"),
                            bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_info_frame,  textvariable=self.var_email,width=20, font=("times new roman ", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number

        phoneNo_label = Label(class_student_info_frame, text="Phone No:", font=("times new roman", 13, "bold"),
                              bg="white")
        phoneNo_label.grid(row=3, column=2, padx=10, sticky=W)

        phoneNo_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_phone, width=20,
                                  font=("times new roman ", 13, "bold"))
        phoneNo_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address

        address_label = Label(class_student_info_frame, text="Address:", font=("times new roman", 13, "bold"),
                              bg="white")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman ", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Teacher name

        teacher_label = Label(class_student_info_frame, text="Teacher Name:", font=("times new roman", 13, "bold"),
                              bg="white")
        teacher_label.grid(row=4, column=2, padx=10, sticky=W)

        teacher_entry = ttk.Entry(class_student_info_frame, textvariable=self.var_teacher, width=20,
                                  font=("times new roman ", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, sticky=W)

        # Radio Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1,command=self.generate_dataset, text="Take photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=7, column=0)

        # self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1, text="No photo Sample",
                                    value="No")
        radiobtn2.grid(row=7, column=1)

        # Button Frame
        btn_frame = Frame(class_student_info_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=40)

        save_btn = Button(btn_frame, width=17, command=self.add_data, text="Save",
                          font=("times new roman ", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, width=17, command=self.update_data,text="Update", font=("times new roman ", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, width=17, command=self.delete_data,text="Delete", font=("times new roman ", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, width=17,command=self.reset_data, text="Reset", font=("times new roman ", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_info_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_sample_btn = Button(btn_frame1, width=35,command=self.generate_dataset, text="Take Photo sample",
                                       font=("times new roman ", 13, "bold"), bg="blue",
                                       fg="white")
        take_photo_sample_btn.grid(row=0, column=0)

        update_photo_sample_btn = Button(btn_frame1, width=35, text="update Photo Sample",
                                         font=("times new roman ", 13, "bold"), bg="blue",
                                         fg="white")
        update_photo_sample_btn.grid(row=0, column=1)

        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\student.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_left = Label(Right_frame, image=self.photoimg_right)
        f_lbl_left.place(x=5, y=0, width=720, height=120)

        # ========= Search System ==========#

        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=700, height=80)

        # Search Bar

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                             bg="white", fg="blue")
        search_label.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17)
        search_combo["values"] = (
            "Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman ", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_btn = Button(search_frame, width=13, text="Search", font=("times new roman ", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, width=13, text="Show All", font=("times new roman ", 10, "bold"), bg="blue",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=2)

        # ======== Table Frame ===========#

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("id",
        "dep", "course", "year", "sem",  "name", "div", "roll", "gender", "dob", "email", "phone", "address",
        "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # --------------- Function Decleration ----------#

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database='attendance_mangement')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                  , (
                                      self.var_std_id.get()
                                      , self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_std_name.get(),
                                      self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get()
                                  ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #----------- Fetch Data --------------------#
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="",
                                       database='attendance_mangement')
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student_data")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)
                conn.commit()
            conn.close()

    #------------ Get Cursor --------------------------#
    def get_cursor(self,event=""):
        cursor_focus =self.student_table.focus()
        content= self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_std_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),

        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update Function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database='attendance_mangement')
                    my_cursor = conn.cursor()

                    my_cursor.execute(
                        "update student_data set dep=%s,course=%s,year=%s,Semester=%s,Student_name=%s,Division=%s,"
                        "Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId =%s",
                        (

                            self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))

                else:
                    if  not update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete pg","Do you want to delete the details of this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database='attendance_mangement')
                    my_cursor = conn.cursor()
                    sql="delete from student_data where StudentId =%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully deleted completed", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #---------------- Generate data set or Take Photo Sample ----------------------#
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database='attendance_mangement')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student_data")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student_data set dep=%s,course=%s,year=%s,Semester=%s,Student_name=%s,Division=%s,"
                    "Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId =%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        id + 1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + h]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed........")

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
