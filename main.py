import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from face_recognition import Face_Recognition
from training_data import train_data_class
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")

        self.root.title("Face Recognition System")

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

        title_lb1 = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman ", 35, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\student.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.student_details)
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2", command=self.student_details, font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\facial_rec.jpeg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.Face_reco)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Detect face", cursor="hand2",command=self.Face_reco ,font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\attandance_face.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,command=self.attendance_management, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance",command=self.attendance_management, cursor="hand2", font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        img7 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\help_desk.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,command=self.help_support, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk",command=self.help_support, cursor="hand2", font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Face button
        img8 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\train_data.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.Training_data)
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2" ,command=self.Training_data, font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=600, width=220, height=40)

        # Photos Face button
        img9 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\photos.jpeg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,command=self.open_img, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos ", cursor="hand2",command=self.open_img, font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=600, width=220, height=40)

        # Developer button
        img10 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\developer.jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,command=self.developer, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer",command=self.developer, cursor="hand2", font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=600, width=220, height=40)

        # Exit button
        img11 = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,command=self.Exit_btn, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit",command=self.Exit_btn, cursor="hand2", font=("times new roman ", 14, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")


    # ------------- Function buttons ------------------#

    def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)

    def Face_reco(self):
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition(self.new_window)


    def Training_data(self):
            self.new_window = Toplevel(self.root)
            self.app = train_data_class(self.new_window)

    def developer(self):
            self.new_window = Toplevel(self.root)
            self.app = Developer(self.new_window)

    def help_support(self):
            self.new_window = Toplevel(self.root)
            self.app = Helpsupport(self.new_window)

    def attendance_management(self):
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)

    def Exit_btn(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
