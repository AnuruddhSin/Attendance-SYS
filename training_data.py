import os
from tkinter import *
from tkinter import ttk
import cv2.face
import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class train_data_class:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1 = Label(self.root, text="Training Data Set",
                          font=("times new roman ", 35, "bold"), bg="gray", fg="green")
        title_lb1.place(x=0, y=0, width=1530, height=55)

        img_top = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\face-off-banner.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="Train Data ", command=self.train_classifier, cursor="hand2", font=("times new roman ", 32, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\face-recognition-system-concept-human-260nw-1139961602.webp")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_left = Label(self.root, image=self.photoimg_bottom)
        f_lbl_left.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)

        # Train the classifier And Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, np.array(ids))
        clf.write("classifier.xml")

        messagebox.showinfo("Result", "Training dataset completed!")

if __name__ == "__main__":
    root = Tk()
    obj = train_data_class(root)
    root.mainloop()
