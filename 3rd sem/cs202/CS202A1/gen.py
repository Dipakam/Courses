
import os
import random

"""We introduce randomization in sudoku, by assigning first row of sudoku a random shuffle of 1 to 9,
 so atleast 9! different sudokus(solved ones)"""

x = [i for i in range(9)]
random.shuffle(x)

var = [0]*81
for n in range(9):
    var[n]=x[n]
with open("cnf.txt", "w") as f:
    count = 9
    for i in range (9):
        for j in range (9):
            if (int(var[9*i+j])>0):
                count = count +1

    f.write ("p cnf 729 "+str(36450+count)+"\n")

    def index(i,j,k):
        return ((i)*9+j)*9+k+1



    for i in range (9):
        for j in range (9):
            if ((var[9*i+j])>0):
                f.write(str(index(i,j,(var[9*i+j])))+" 0\n")


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
            if (int(x1/3) == int(x2/3)):
                for y1 in range (9):
                    for y2 in range (9):
                        if (int(y1/3) ==int(y2/3)):
                            if ((x1 != x2) or (y1 != y2)):
                                for z in range (9):
                                    f.write ("-"+str(index(x1,y1,z))+" -"+str(index(x2,y2,z))+" 0\n")
f.close ()
os.system("minisat cnf.txt out.txt")
array = []
with open("out.txt", "r") as fo:
    outp = fo.read().rsplit("\n")

    if outp[0] == "SAT":
        var = outp[1].rsplit(" ")
        for i in range(9):
            for j in range(9):

                for k in range(9):
                    if (int(var[index(i,j,k)-1]) > 0):
                        array.append(k+1)
                        continue;


"""Till now we made a random complete Sudoku, now we randomly remove elements till we arrive at a minimal solution"""

var1 = []
var2 = []

for x in array:
    var1.append((x))
    var2.append((x))


"""function to test uniqueness of solution to a given sudoku"""

def test1(a):

    def index(i,j,k):
        return ((i)*9+j)*9+k+1

    with open("cnf1.txt", "w") as f:
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
                if (int(x1/3) == int(x2/3)):
                    for y1 in range (9):
                        for y2 in range (9):
                            if (int(y1/3) ==int(y2/3)):
                                if ((x1 != x2) or (y1 != y2)):
                                    for z in range (9):
                                        f.write ("-"+str(index(x1,y1,z))+" -"+str(index(x2,y2,z))+" 0\n")
    f.close ()
    os.system("minisat cnf1.txt out2.txt")

    with open("out2.txt", "r") as fo:
        outp = fo.read().rsplit("\n")

        if outp[0] == "SAT":
            return 0
        else:
            #print("1 .......\n\n")
            return 1
        fo.close()


"""We remove random elements, ie with a random shuffle of subscripts, if uniqueness is disturbed we put back the removed element"""

b = [i for i in range(81)]

random.shuffle(b)

i = 0
while(True):
    var2[b[i]] = 0

    if(test1(var2) == 0):
        var2[b[i]] = var1[b[i]]
    i=i+1


    if i==81:
        break

print("Random minimal sudoku+ is ...\n")
for i in range(9):
    for j in range(9):
        if(var2[i*9+j] == 0):
            print(". ",end = "")
        else:
            print(var2[i*9+j],end=" ")
    print("\n")

print("The solution to the minimal sudoku+ is .....\n")
for i in range(9):
    for j in range(9):
        print(array[i*9+j],end=" ")
    print("\n")
