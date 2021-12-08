# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:43:59 2021

@author: IDEA3C
"""

# Question (1) 
file=open("C:\\Users\\IDEA3C\\Downloads\\IMDB-Movie-Data.csv","rt",encoding="utf-8")
data=file.readlines()
data.pop(0)

list1=[]
n=0
for i in range(len(data)):
    list1.append(data[i])
    list1=list1[0].split(",")
    if n<3 and "2016" in list1:
        print(list1[1])
        n+=1
    list1.clear()
file.close() 

# Question (2)
file=open("C:\\Users\\IDEA3C\\Downloads\\IMDB-Movie-Data.csv","rt",encoding="utf-8")
data=file.readlines()
data.pop(0)

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in range(len(data)):
    list1.append(data[i])
    list1=list1[0].split(",")
    list2.append(list1[4])
    list1.clear()
for j in range(len(list2)):
    list3.append(list2[j])
    list3=list3[0].split("|")   #把每筆資料的演員分別放在list裡
    list4.append(list3)    
    list3.clear()
for element in list4:
    if element not in list5:
        list5.append(element)   #一個演員出現一次
file.close()

# Question (3)
file=open("C:\\Users\\IDEA3C\\Downloads\\IMDB-Movie-Data.csv","rt",encoding="utf-8")
data=file.readlines()
data.pop(0)

list1=[]
list2=[]
for i in range(len(data)):
    list1.append(data[i])
    list1=list1[0].split(",")
    if "Emma Watson" in list1[4]:
        list2.append(list1[7])
    list1.clear()
int_list=list(map(float,list2))
sum1=sum(int_list)
print(sum1/len(int_list))
file.close()

# Quesstion (4)
file=open("C:\\Users\\IDEA3C\\Downloads\\IMDB-Movie-Data.csv","rt",encoding="utf-8")
data=file.readlines()
data.pop(0)

list1=[]
list2=[]
list3=[]
for i in range(len(data)):
    list1.append(data[i])
    list1=list1[0].split(",")
    list2.append(list1[3])
    for element in list2:
        if element not in list3:
            list3.append(element)  #每個導演名字(出現一次)
    list1.clear()

file.close()
        