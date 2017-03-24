import sys, cv2 as cv
import numpy as np
import csv, os
os.system('cls')
f=open('emotion1pic.csv','r+')
objs = []
for line in csv.reader(open('emotion1pic.csv', 'r'), delimiter=','):
    objs.append(line)
firstRow = objs[1:]#записываем строки с 1 строки до конца
print(firstRow)
np.array(firstRow)
new1 = np.array(firstRow)[:,1:2] #получил вектор, 2304 символа. Теперь нужно
#перевести это в матрицу размера 48x48, числа разделены пробелами
#print(new1.shape)

k=0
t=0
h=48
arr = np.zeros((48, 48))
ints=[int(s) for s in str(new1[0,0]).split()]#делаем массив из 2304 чисел, для 1 картинки
print(ints)

for i in range(48):#реорганизуем массив в матрицу
    for j in range(48):
        arr[i][j] = ints[j + t * h] #reorganize integral image
    t+=1
print (arr)
picnumber='00001'
emoNumber='0'
adirectory='emotionimage'

cv.imwrite("%s/emo_%s_pic%s.jpg" % (adirectory, emoNumber, picnumber), arr)
#cv.imwrite('emo-0-pic00001.png', arr)#записываем матрицу в виде картинки, получаем 48х48 пикселей
