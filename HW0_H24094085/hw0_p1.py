# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:57:27 2021

@author: IDEA3C
"""


    
def Multiply(p1, p2):
    coefficient_1 = []
    exponent_1 = []
    coefficient_2 = []
    exponent_2 = []
    # 1,-1 for coefficient. 0 for coefficient has saved. 2 for meet a character
    flag = 1
    variable = ''

    # seperate coefficient and variables, coefficient
    # first polynomial
    for a in p1:
        if a.isdigit() and flag != 0:
            coefficient_1.append(int(a)*flag)
            flag = 0
        elif a == '+' or a == '-' or a == ')':
            if a == '+':
                flag = 1
            elif a == '-':
                flag = -1
            exponent_1.append(variable)
            variable = ''
        else:
            if flag != 0:
                coefficient_1.append(1*flag)
                flag = 0
            variable += a

    # second polynomial
    flag = 1
    for a in p2:
        if a.isdigit() and flag != 0:
            coefficient_2.append(int(a)*flag)
            flag = 0
        elif a == '+' or a == '-' or a == ')':
            if a == '+':
                flag = 1
            elif a == '-':
                flag = -1
            exponent_2.append(variable)
            variable = ''
        else:
            if flag != 0:
                coefficient_2.append(1*flag)
                flag = 0
            variable += a
    # Multiply term by term
    coefficient = []
    exponent = []
    # 1 for no problem. 2 for backward 1. 3 for forward 1. 6 for both 1
    flag = 1
    variable = ''
    for i,c1 in enumerate(coefficient_1):
        for j,c2 in enumerate(coefficient_2):
            # coefficient
            c = c1 * c2
            coefficient.append(c)

            # variables and exponent

            e = exponent_1[i] + exponent_2[j]
    #        print(i,j,exponent_1[i],exponent_2[j],e)
            for k,v in enumerate(e):  # Note : the for loop will traverse the old e
                if k >= len(e):
                    pass                    #do nothing
                elif e[k].isalpha():        #str.isalpha -> 字串裡都是字母
                    flag = 1
                    pos = e.find(e[k], k+1)    
                    # find duplication
                    if pos >= 0:
                        # polynomial 1 exponent
                        if k+1 >= len(e):
                            t = 1
                            flag += 2
                        elif e[k+1].isdigit():
                            t = int(e[k+1])
                        else:
                            t = 1
                            flag += 2
                        # polynomial 2 exponent
                        if pos+1 >= len(e):
                            t += 1
                            flag *= 2
                        elif e[pos+1].isdigit():
                            t += int(e[pos+1])
                        else:
                            t += 1
                            flag *= 2
                        # update the new variable and exponent
                        new_e = e[:k+1] + str(t)
                        # forward update
                        if flag == 3 or flag == 6:
                            new_e += e[k+1:pos]
                        else:
                            new_e += e[k+2:pos]
                        # backward truncate
                        if flag == 2 or flag ==6:
                            new_e += e[pos+1:]
                        else:
                            new_e += e[pos+2:]
                        e = new_e
            exponent.append(e)

    # rearrange the order of variable, exponent
    for i in range(len(exponent)):
        # construct the variable, exponent to a dictionary
        dic = {}
        for j in range(len(exponent[i])):
            if exponent[i][j].isalpha() and (j+1 >= len(exponent[i]) or         exponent[i][j + 1].isalpha()):
                dic[exponent[i][j]] = 1
            elif exponent[i][j].isalpha() and exponent[i][j+1].isdigit():
                dic[exponent[i][j]] = int(exponent[i][j+1])
           
           
        
x=str(input("Please input the polynomials:"))
while True:
    if x=="":
        break
    b=x.split(")(")
    list1=str(b[0])
    list1.replace("(","")
    list2=str(b[1])
    list2.replace(")","")
n=b.count(")")
# Multiply two function at a time
for i in range(n-1):
    t1 = 0
    p1_start = x.index('(', t1)
    p1_end = x.index(')', t1)
    t2 = p1_end
    p2_start = x.index('(', t2 + 1)
    p2_end = x.index(')', t2 + 1)
    t1 = p2_end+1

    p1 = x[p1_start + 1: p1_end + 1]
    print(p1)
    p2 = x[p2_start + 1: p2_end + 1]
    print(p2)

  