

array= ['8', '2', '4', 0, 0, 0, 0, 0, 0, 0, 0, '2', '8', 0, 0, 0, '6', 0, '1', '4', 0, 0, 0, 0, 0, '3', 0, 0, 0, 0, 0, 0, 0, '3', 0, 0, '6', 0, 0, 0, 0, 0, 0, 0, '7', 0, 0, 0, 0, 0, 0, '6', '4', '3', 0, 0, 0, 0, 0, '8', 0, '2', '1', '7', 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, 0, '3', '4', '2', '1', 0, '6']
sol =[4, 6, 9, 3, 7, 8, 5, 2, 1, 3, 9, 6, 2, 1, 4, 7, 8, 5, 6, 2, 5, 1, 4, 9, 3, 7, 8, 2, 4, 1, 8, 3, 6, 9, 5, 7, 7, 1, 3, 4, 2, 5, 8, 6, 9, 1, 3, 2, 5, 8, 7, 4, 9, 6, 8, 5, 4, 7, 9, 1, 6, 3, 2, 5, 7, 8, 9, 6, 3, 2, 1, 4, 9, 8, 7, 6, 5, 2, 1, 4, 3]

import random
import os
a =[[],[],[],[],[],[],[],[],[]]
for i in range (9):
    for j in range(9):
        a[i].append(sol[i*9+j])
print(a)
flag=1
for i in range(9):
    for j in range(9):
        for k in range(9):
            if(j!=k):
                if(a[i][j]==a[i][k]):
                    flag=0
                    print(i,j,k)
                if(a[j][i]==a[k][i]):
                    flag=0
                    print(i,j,k)

for i in range(9):
    for j in range(9):
        if(i!=j):
            if(a[i][i]==a[j][j]):
                flag=0
                print(i,j)
            if(a[i][8-i]==a[j][8-j]):
                flag=0
                print(i,j)

for i1 in range(9):
    for i2 in range(9):
        if((i1/3==i2/3) and (i1 != i2)):
            for j1 in range(9):
                for j2 in range(9):
                    if(j1/3==j2/3):
                        if((a[i1][j1]==a[i2][j2]) and (j1!=j2)):
                            flag=0
                            print(i1,j1,i2,j2)

print(flag)
