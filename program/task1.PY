import sys
from math import isnan
from re import L
import numpy as np
import matplotlib.pyplot as mtp
import imageio.v2 as imgageio
import matplotlib.pyplot as plt
import cv2
import sys
sys.setrecursionlimit(17500)


def newone(filename):
    file = open(filename, 'r')
    newm = file.readlines()
    file.close
    return newm


def implemnt(filename):

    o = newone(filename)
    mylist = []

    # changing from normal list to list 2 dimensions
    for id, i in enumerate(o):
        j = i.partition('\n')
        mylist.append(float(j[0]))

    # print(mylist)

    mylist_4 = []
    while mylist != []:
        mylist_4.append(mylist[:4])
        mylist = mylist[4:]

    return mylist_4
# calculate lenght of our matrice


# creation matrix null
def get_lenght(image):
    img = imgageio.imread(image)
    img = img.tolist()
    lenght_img0 = len(img)
    return lenght_img0


# NULL_MATRIXE = [[0 for j in range(get_lenght("11.png"))]
#                 for i in range(get_lenght("11.png"))]
def create_null_m(image):
    my_matrixe = np.zeros((get_lenght(image), get_lenght(image)))
    return my_matrixe
