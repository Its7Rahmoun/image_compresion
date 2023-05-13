from tkinter import *
from task1 import implemnt
from task1 import create_null_m
from task0 import getm
from tkinter import filedialog
import os
import cv2
import random
from os.path import exists
import string
import sys


sys.setrecursionlimit(30500)

print(sys.getrecursionlimit())


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("compressionApp")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("python.ico")
        self.window.config(background='#41B77F')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle("ecart type")
        self.input_ecartype = Entry(self.frame, font=("Courrier", 40), bg='white',
                                    fg='#41B77F')
        self.input_ecartype.pack()

        self.create_subtitle("ur new image name")
        self.input_newimage = Entry(self.frame, font=("Courrier", 40), bg='white',
                                    fg='#41B77F')
        self.input_newimage.pack()

        self.create_button()

    def create_title(self):
        label_title = Label(self.window, text="compression App", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self, s):
        label_subtitle = Label(self.frame, text=s, font=("Courrier", 10), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def create_button(self):
        yt_button = Button(self.frame, text="get ur image", font=(
            "Courrier", 25), bg='white', fg='#41B77F', command=self.getimage)
        yt_button.pack(pady=25, fill=X)

    def getimage(self):
        bool1 = False
        self.image = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image file", filetypes=(
            ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("ALL Files", "*.*")))
        print(self.image)
        self.ecarttype = self.input_ecartype.get()
        self.newimage = self.input_newimage.get()
        self.filename = ''.join(random.choices(string.ascii_uppercase +
                                               string.digits, k=4))+"1.txt"
        print(self.filename)
        getm(self.image, str(
            self.filename), float(self.ecarttype))
        while (True):
            file_exists = exists(self.filename)
            if file_exists:
                break
        mylist_4 = implemnt(str(self.filename))
        my_matrixe = create_null_m(str(self.image))

        def getmatrixe(b):

            for i in range(int(mylist_4[b][0]), int(mylist_4[b][2]+int(mylist_4[b][0]))):
                for j in range(int(mylist_4[b][1]), int(mylist_4[b][2]+int(mylist_4[b][1]))):
                    my_matrixe[i][j] = int(mylist_4[b][3])
            b = b+1
            if b < len(mylist_4):
                # print(b)
                getmatrixe(b)
            return my_matrixe, True
        self.ourlistcompressed, bool1 = getmatrixe(0)
        if bool1:
            self.create_subtitle("ur image has been created")
        self.window.destroy
        image1 = cv2.imwrite(str(self.newimage), self.ourlistcompressed)
        img = cv2.imread(self.newimage, cv2.IMREAD_ANYCOLOR)
        file_size = os.path.getsize(str(self.image))
        file_size_new = os.path.getsize(str(self.newimage))
        self.gange = abs(file_size-file_size_new)
        print(self.gange)
        self.create_subtitle("gain is "+str(self.gange)+" bytes")
        cv2.imshow("", img)


# afficher
app = MyApp()
app.window.mainloop()
