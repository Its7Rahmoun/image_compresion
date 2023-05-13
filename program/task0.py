import numpy as np
import imageio.v2 as imgageio


correct = []
lm = [0, 0]


def comression(A, lm, ecar_type):
    l1 = []
    l11 = []
    l2 = []
    l22 = []
    l3 = []
    l33 = []
    l4 = []
    l44 = []
    for id1, i in enumerate(A):

        for id2, j in enumerate(i):
            if id2 <= int(len(A)/2-1) and id1 <= int(len(A)/2-1):
                l1.append(j)
                if lm == [0, 0]:
                    l11.append([id1, id2])
                else:
                    a = lm[0]
                    b = lm[1]
                    l11.append((id1+a, id2+b))
            if id2 > int(len(A)/2-1) and id1 <= int(len(A)/2-1):
                l2.append(j)
                if lm == [0, 0]:
                    l22.append([id1, id2])
                else:
                    l22.append((id1+lm[0], id2+lm[1]))
            if id2 <= int(len(A)/2-1) and id1 > int(len(A)/2-1):
                l3.append(j)
                if lm == [0, 0]:
                    l33.append([id1, id2])
                else:
                    l33.append((id1+lm[0], id2+lm[1]))
            if id2 > int(len(A)/2-1) and id1 > int(len(A)/2-1):
                l4.append(j)
                if lm == [0, 0]:
                    l44.append([id1, id2])
                else:
                    l44.append((id1+lm[0], id2+lm[1]))

    l = int(len(A)/2)
    mat1 = []
    while l1 != []:
        mat1.append(l1[:l])
        l1 = l1[l:]
    mat2 = []
    while l2 != []:
        mat2.append(l2[:l])
        l2 = l2[l:]
    mat3 = []
    while l3 != []:
        mat3.append(l3[:l])
        l3 = l3[l:]
    mat4 = []
    while l4 != []:
        mat4.append(l4[:l])
        l4 = l4[l:]

    if np.std(mat1) < ecar_type or len(mat1) <= 2:
        res = [sum(idx) / len(idx) for idx in zip(*mat1)]
        res = sum(res) / len(res)
        correct.append([l11[0][0], l11[0][1], int(len(mat1)), res])
    else:

        lm1 = [0, 0]

        lm1[0] = l11[0][0]
        lm1[1] = l11[0][1]
        comression(mat1, lm1, ecar_type)
    if np.std(mat2) < ecar_type or len(mat2) <= 2:
        res = [sum(idx) / len(idx) for idx in zip(*mat2)]
        res = sum(res) / len(res)
        correct.append([l22[0][0], l22[0][1], int(len(mat2)), res])
    else:

        lm2 = [0, 0]

        lm2[0] = l22[0][0]
        lm2[1] = l22[0][1]
        comression(mat2, lm2, ecar_type)
    if np.std(mat3) < ecar_type or len(mat3) <= 2:
        res = [sum(idx) / len(idx) for idx in zip(*mat3)]
        res = sum(res) / len(res)
        correct.append([l33[0][0], l33[0][1], int(len(mat3)), res])
    else:

        lm3 = [0, 0]
        lm3[0] = l33[0][0]
        lm3[1] = l33[0][1]

        comression(mat3, lm3, ecar_type)
    if np.std(mat4) < ecar_type or len(mat4) <= 2:
        res = [sum(idx) / len(idx) for idx in zip(*mat4)]
        res = sum(res) / len(res)
        correct.append([l44[0][0], l44[0][1], int(len(mat4)), res])
    else:

        lm4 = [0, 0]
        lm4[0] = l44[0][0]
        lm4[1] = l44[0][1]

        comression(mat4, lm4, ecar_type)


def is_power_of_two(number: int) -> bool:
    while number != 1:
        if number % 2:
            return False
        number /= 2
    return True


def moyenne(l):
    s = 0
    for i in range(len(l)):
        s = s+l[i]
    s = s/len(l)
    return s


def moyen(m):
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = int(moyenne(m[i][j]))
    return m


def getm(image, filename, ecar_type):
    img = imgageio.imread(image)
    img = img.tolist()
    lenght_img0 = len(img)
    lenght_img1 = len(img[0])
    if lenght_img1 != lenght_img0:
        print("image does not have  the  Same Height and Width ")
    else:
        if is_power_of_two(lenght_img0) and is_power_of_two(lenght_img1):
            m = moyen(img)
            comression(m, lm, ecar_type)
            file = open(filename, 'w')
            for i in correct:
                for j in i:
                    file.write(str(j) + "\n")
            file.close

        else:
            print("width or height of image is not power of two")


# print(correct)
# getm("1.png", "my.txt", 65)
