import os

"""Opening input File and reading soduko to solve"""

with open("quest.txt","r") as inpt:
    inp = inpt.read()
    array = inp.rsplit("\n")
    var = []
    for x in array:
        str1 = x.rsplit(" ")
        for c in str1:
            if (c == "."):
                var.append("0")
            else:
                var.append(c)

inpt.close()

"""Writing on cnf.txt which would be fed to minisat to check if it is satisfiable,
 we have 729 variables, and all conditions implemented in CNF form"""

with open("cnf.txt", "w") as f:
    count = 0
    for i in range (9):
        for j in range (9):
            if (int(var[9*i+j])>0):
                count = count +1

    f.write ("p cnf 729 "+str(18346+count)+"\n")

    def index(i,j,k):
        return ((i)*9+j)*9+k+1



    for i in range (9):
        for j in range (9):
            if (int(var[9*i+j])>0):
                f.write(str(index(i,j,int(var[9*i+j])-1))+" 0\n")


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

"""Parsing minisat output file"""

with open("out.txt", "r") as fo:
    outp = fo.read().rsplit("\n")

    if outp[0] == "SAT":
        var = outp[1].rsplit(" ")
        print("Satisfiable")
        for i in range(9):
            for j in range(9):

                for k in range(9):
                    if (int(var[index(i,j,k)-1]) > 0):
                        print (k+1,end = " ")
                        continue;
            print("\n")
    else:
        print ("Unsatisfiable")
