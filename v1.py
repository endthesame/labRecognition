from PIL import Image
import numpy as np
import math as m
import os

# 0 - black, 255 - white

def toBnW(ar):
    arr = np.array([])
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            arr = np.append(arr, ar[i][j][0])  
            # if ar[i][j][0] != 0:
            #     arr = np.append(arr, 255)
            # else:
            #     arr = np.append(arr, 0)                                            
    return(arr)

def openToMatrix(name):
    cwd = os.getcwd()
    ideal = Image.open(r"{}/files/{}.png".format(cwd , name))
    ar = np.array(ideal)
    ar = toBnW(ar)
    return(ar)

def coreFind(name1 , name2, name3):
    core = (name1 + name2 + name3) / 3
    return(core)

#расстояние обычного евклида (навсякий случай)

def euclideanDis(core , unclassed):
    a = core - unclassed
    b = a.transpose()
    c = np.dot(b,a)
    transpose = m.sqrt(c)
    return(transpose)

#расстояние евклида махаланобиса

def eucMahalanobis(core , unclassed, covariance):
    a = core - unclassed
    b = a.transpose()
    c = np.dot(a,covariance)
    d = np.dot(c, b)
    transpose = m.sqrt(d)
    return(transpose)

#функция нахождения матрицы ковариации умноженной на еденичную матрицу 

def covariance(core, ideal1, ideal2, ideal3):
    cov = [[0 for j in range(100)]for i in range (100)]
    for i in range(100):
        for j in range(100):
            cov[i][j] = (1/2)*((ideal1[i] - core[i])*(ideal1[j] - core[j]) + (ideal2[i] - core[i])*(ideal2[j] - core[j]) + (ideal3[i] - core[i])*(ideal3[j] - core[j]))
    emat = np.eye(100)
    ress = (cov + emat)
    res = np.linalg.inv(ress)
    return(res)
    

def disToClass(dis1,dis2,dis3, dis4):
    if min(dis1,dis2,dis3,dis4) == dis1:
        tp = "a"
    if min(dis1,dis2,dis3,dis4) == dis2:
        tp = "b"
    if min(dis1,dis2,dis3,dis4) == dis3:
        tp = "w"
    if min(dis1,dis2,dis3,dis4) == dis4:
        tp = "z"
    return tp

def classAppend(tp,unclassed,classA, classB,classW,classZ,name):
    if tp == "a":
        classA.append(unclassed)
        print("Изображение {} относится к классу A".format(name))
    if tp == "b":
        classB.append(unclassed)
        print("Изображение {} относится к классу B".format(name))
    if tp == "w":
        classW.append(unclassed)
        print("Изображение {} относится к классу W".format(name))
    if tp == "z":
        classZ.append(unclassed)
        print("Изображение {} относится к классу Z".format(name))      

#Создание матриц идеальных и неклассифицированных изображений

idealA1 = openToMatrix("ideal_A_1")
idealA2 = openToMatrix("ideal_A_2")
idealA3 = openToMatrix("ideal_A_3")

idealB1 = openToMatrix("ideal_B_1")
idealB2 = openToMatrix("ideal_B_2")
idealB3 = openToMatrix("ideal_B_3")

idealW1 = openToMatrix("ideal_W_1")
idealW2 = openToMatrix("ideal_W_2")
idealW3 = openToMatrix("ideal_W_3")

idealZ1 = openToMatrix("ideal_Z_1")
idealZ2 = openToMatrix("ideal_Z_2")
idealZ3 = openToMatrix("ideal_Z_3")

unclassed1 = openToMatrix("unclassed_1")
unclassed2 = openToMatrix("unclassed_2")
unclassed3 = openToMatrix("unclassed_3")
unclassed4 = openToMatrix("unclassed_4")

#вывод матриц распозноваемых объектов

print("Матрица распознаваемого объекта unclassed1 - {}".format(unclassed1))
print("Матрица распознаваемого объекта unclassed2 - {}".format(unclassed2))
print("Матрица распознаваемого объекта unclassed3 - {}".format(unclassed3))
print("Матрица распознаваемого объекта unclassed4 - {}".format(unclassed4))

print()

#Создание классов и добавление в них идеальных

classA = [idealA1, idealA2, idealA3]
classB = [idealB1, idealB2, idealB3]
classW = [idealW1, idealW2, idealW3]
classZ = [idealZ1, idealZ2, idealZ3]

#создание ядер каждого класса

coreA = coreFind(idealA1, idealA2, idealA3)
coreB = coreFind(idealB1, idealB2, idealB3)
coreW = coreFind(idealW1, idealW2, idealW3)
coreZ = coreFind(idealZ1, idealZ2, idealZ3)

#вывод ядер всех классов

print("Ядро класса A - {}".format(coreA))
print("Ядро класса B - {}".format(coreB))
print("Ядро класса W - {}".format(coreW))
print("Ядро класса Z - {}".format(coreZ))

print()

# матрица ковариации для каждого класса

covA = covariance(coreA, idealA1, idealA2, idealA3)
covB = covariance(coreB, idealB1, idealB2, idealB3)
covW = covariance(coreW, idealW1, idealW2, idealW3)
covZ = covariance(coreZ, idealZ1, idealZ2, idealZ3)

#расстояние обычного евклида (навсякий случай)

# DisAtoUnclass1 = euclideanDis(coreA, unclassed1)
# DisBtoUnclass1 = euclideanDis(coreB, unclassed1)
# DisWtoUnclass1 = euclideanDis(coreW, unclassed1)
# DisZtoUnclass1 = euclideanDis(coreZ, unclassed1)

# DisAtoUnclass2 = euclideanDis(coreA, unclassed2)
# DisBtoUnclass2 = euclideanDis(coreB, unclassed2)
# DisWtoUnclass2 = euclideanDis(coreW, unclassed2)
# DisZtoUnclass2 = euclideanDis(coreZ, unclassed2)

# DisAtoUnclass3 = euclideanDis(coreA, unclassed3)
# DisBtoUnclass3 = euclideanDis(coreB, unclassed3)
# DisWtoUnclass3 = euclideanDis(coreW, unclassed3)
# DisZtoUnclass3 = euclideanDis(coreZ, unclassed3)

# DisAtoUnclass4 = euclideanDis(coreA, unclassed4)
# DisBtoUnclass4 = euclideanDis(coreB, unclassed4)
# DisWtoUnclass4 = euclideanDis(coreW, unclassed4)
# DisZtoUnclass4 = euclideanDis(coreZ, unclassed4)

#дистанции от каждого ядра каждого класса до неклассифицированных матриц(изображений)

DisAtoUnclass1 = eucMahalanobis(coreA, unclassed1, covA)
DisBtoUnclass1 = eucMahalanobis(coreB, unclassed1, covB)
DisWtoUnclass1 = eucMahalanobis(coreW, unclassed1, covW)
DisZtoUnclass1 = eucMahalanobis(coreZ, unclassed1, covZ)

DisAtoUnclass2 = eucMahalanobis(coreA, unclassed2, covA)
DisBtoUnclass2 = eucMahalanobis(coreB, unclassed2, covB)
DisWtoUnclass2 = eucMahalanobis(coreW, unclassed2, covW)
DisZtoUnclass2 = eucMahalanobis(coreZ, unclassed2, covZ)

DisAtoUnclass3 = eucMahalanobis(coreA, unclassed3, covA)
DisBtoUnclass3 = eucMahalanobis(coreB, unclassed3, covB)
DisWtoUnclass3 = eucMahalanobis(coreW, unclassed3, covW)
DisZtoUnclass3 = eucMahalanobis(coreZ, unclassed3, covZ)

DisAtoUnclass4 = eucMahalanobis(coreA, unclassed4, covA)
DisBtoUnclass4 = eucMahalanobis(coreB, unclassed4, covB)
DisWtoUnclass4 = eucMahalanobis(coreW, unclassed4, covW)
DisZtoUnclass4 = eucMahalanobis(coreZ, unclassed4, covZ)


#вывод расстояния каждого объекта до каждого класса

print("Расстоние от А-класс до unclassed1", DisAtoUnclass1)
print("Расстоние от B-класс до unclassed1", DisBtoUnclass1)
print("Расстоние от W-класс до unclassed1", DisWtoUnclass1)
print("Расстоние от Z-класс до unclassed1", DisZtoUnclass1)

print("Расстоние от А-класс до unclassed2", DisAtoUnclass2)
print("Расстоние от B-класс до unclassed2", DisBtoUnclass2)
print("Расстоние от W-класс до unclassed2", DisWtoUnclass2)
print("Расстоние от Z-класс до unclassed2", DisZtoUnclass2)

print("Расстоние от А-класс до unclassed3", DisAtoUnclass3)
print("Расстоние от B-класс до unclassed3", DisBtoUnclass3)
print("Расстоние от W-класс до unclassed3", DisWtoUnclass3)
print("Расстоние от Z-класс до unclassed3", DisZtoUnclass3)

print("Расстоние от А-класс до unclassed3", DisAtoUnclass4)
print("Расстоние от B-класс до unclassed3", DisBtoUnclass4)
print("Расстоние от W-класс до unclassed3", DisWtoUnclass4)
print("Расстоние от Z-класс до unclassed3", DisZtoUnclass4)

print()

# определение к какому классу относятся неклассифицированные матрицы

tp1 = disToClass(DisAtoUnclass1, DisBtoUnclass1, DisWtoUnclass1, DisZtoUnclass1)
tp2 = disToClass(DisAtoUnclass2, DisBtoUnclass2, DisWtoUnclass2, DisZtoUnclass2)
tp3 = disToClass(DisAtoUnclass3, DisBtoUnclass3, DisWtoUnclass3, DisZtoUnclass3)
tp4 = disToClass(DisAtoUnclass4, DisBtoUnclass4, DisWtoUnclass4, DisZtoUnclass4)

naming1 = "unclassed_1"
naming2 = "unclassed_2"
naming3 = "unclassed_3"
naming4 = "unclassed_4"

# Добавление неклассфифицированных матриц в класс

classAppend(tp1,unclassed1,classA, classB, classW, classZ,naming1)
classAppend(tp2,unclassed2,classA, classB, classW, classZ,naming2)
classAppend(tp3,unclassed3,classA, classB, classW, classZ,naming3)
classAppend(tp4,unclassed4,classA, classB, classW, classZ,naming4)
