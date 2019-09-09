import random
import os
x = input()
var1 = x.rsplit(", ")
var2 = x.rsplit(", ")
print(var1)
print(var2)






flag = 1

def test(a):

    def index(i,j,k):
        return ((i)*9+j)*9+k+1

    with open("cnf.txt", "w") as f:
        count = 0
        for i in range (9):
            for j in range (9):
                if (int(a[9*i+j])>0):
                    count = count +1

        f.write ("p cnf 729 "+str(18346+count)+"\n")



        for i in range (9):
            for j in range (9):
                if (int(a[9*i+j])>0):
                    f.write(str(index(i,j,int(a[9*i+j])-1))+" 0\n")

        for i in range(9):
            for j in range(9):
                f.write("-"+str(index(i,j,int(var1[9*i+j]))-1)+" ")

        f.write("0\n")


        for x in range (9):
            for y in range (9):
                for z in range (9):
                    f.write (str(index(x,y,z))+" ")

                f.write ("0\n")

        for x in range (9):
            for z in range (9):
                for y1 in range (9):
                    for y2 in range (9):
                        if (y1 != y2):
                            f.write ("-"+str(index(x,y1,z))+" -"+str(index(x,y2,z))+" 0\n")

        for x in range (9):
            for y in range (9):
                for z1 in range (9):
                    for z2 in range (9):
                        if (z1 != z2):
                            f.write ("-"+str(index(x,y,z1))+" -"+str(index(x,y,z2))+" 0\n")


        for y in range (9):
            for z in range (9):
                for x1 in range (9):
                    for x2 in range (9):
                        if (x1 != x2):
                            f.write ("-"+str(index(x1,y,z))+" -"+str(index(x2,y,z))+" 0\n")

        for x in range (9):
            for y in range (9):
                if (x < y):
                    for z in range (9):
                        f.write ("-"+str(index(x,x,z))+" -"+str(index(y,y,z))+" 0\n")


        for x in range (9):
            for y in range (9):
                if (x < y):
                    for z in range (9):
                        f.write ("-"+str(index(x,8-x,z))+" -"+str(index(y,8-y,z))+" 0\n")

        for x1 in range (9):
            for x2 in range (9):
                if ((x1/3) == (x2/3)):
                    for y1 in range (9):
                        for y2 in range (9):
                            if ((y1/3) ==(y2/3)):
                                if ((x1 != x2) or (y1 != y2)):
                                    for z in range (9):
                                        f.write ("-"+str(index(x1,y1,z))+" -"+str(index(x2,y2,z))+" 0\n")
    f.close ()
    os.system("minisat cnf.txt out.txt")

    with open("out.txt", "r") as fo:
        outp = fo.read().rsplit("\n")

        if outp[0] == "SAT":
            return 0
        else:
            return 1
        fo.close()


b = [i for i in range(81)]

random.shuffle(b)

i = 0
while(True):
    var2[b[i]] = 0
    #print (var2)
    if(test(var2) == 0):
        var2[b[i]] = var1[b[i]] #could use just swap mechanism
    i=i+1
    if (i==81):
        print (var2)

    if i==81:
        break
