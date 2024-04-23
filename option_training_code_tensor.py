# import os
# from tkinter import *
# from tkinter import messagebox
# import numpy as np
# import cv2
# from PIL import Image, ImageTk
# import mysql.connector
# import tensorflow as tf
# import keras
# from keras.models import load_model
#
# class train_data_class:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")
#
#         title_lb1 = Label(self.root, text="Training Data Set",
#                           font=("times new roman ", 35, "bold"), bg="white", fg="green")
#         title_lb1.place(x=0, y=0, width=1530, height=45)
#
#         img_top = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\facial_recognition.jpg")
#         img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#
#         f_lbl_left = Label(self.root, image=self.photoimg_top)
#         f_lbl_left.place(x=0, y=55, width=1530, height=325)
#
#         b1_1 = Button(self.root, text="Train Data ",command=self.train_classifier, cursor="hand2", font=("times new roman ", 32, "bold"),
#                       bg="darkblue", fg="white")
#         b1_1.place(x=0, y=380, width=1530, height=60)
#
#         img_bottom = Image.open(r"D:\Projects\ML Project\ATMS_GUI\Resources\facial_recognition.jpg")
#         img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
#
#         f_lbl_left = Label(self.root, image=self.photoimg_bottom)
#         f_lbl_left.place(x=0, y=440, width=1530, height=325)
#
#     def train_classifier(self):
#         data_dir = "data"
#         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
#
#         faces = []
#         ids = []
#
#         for image in path:
#             img = Image.open(image).convert('L')  # Gray scale image
#             imageNp = np.array(img, 'uint8')
#             id = int(os.path.split(image)[1].split('.')[1])
#
#             faces.append(imageNp)
#             ids.append(id)
#
#         ids = np.array(ids)
#
#         # Load pre-trained FaceNet model
#         try:
#             facenet_model = load_model("facenet_model.h5", compile=True)
#             messagebox.showinfo("Result", "Model loaded successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to load model: {e}")
#
#         # Extract face embeddings using FaceNet
#         def extract_face_embeddings(face):
#             # Resize image to 160x160 as required by FaceNet
#             face = cv2.resize(face, (160, 160))
#             # Scale pixel values
#             face = face.astype('float32')
#             # Standardize pixel values across channels (global normalization)
#             mean, std = face.mean(), face.std()
#             face = (face - mean) / std
#             # Expand dimensions to fit the model input shape
#             face = np.expand_dims(face, axis=0)
#             # Generate embeddings
#             embeddings = facenet_model.predict(face)
#             return embeddings
#
#         # Extract face embeddings for each face
#         embeddings_list = []
#         for face in faces:
#             embeddings = extract_face_embeddings(face)
#             embeddings_list.append(embeddings)
#
#         # Train your classifier using the extracted embeddings
#         # Add your classifier training code here
#
#         messagebox.showinfo("Result", "Training dataset completed!")
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = train_data_class(root)
#     root.mainloop()
