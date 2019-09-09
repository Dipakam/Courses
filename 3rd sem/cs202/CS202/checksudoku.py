array = ['9', 0, '3', 0, 0, '7', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '5', 0, '6', 0, 0, '2', 0, 0, 0, 0, 0, 0, '4', '3', 0, 0, 0, 0, 0, 0, 0, 0, '9', 0, 0, 0, '7', '8', 0, 0, 0, '2', 0, 0, '6', '5', 0, 0, 0, 0, 0, 0, 0, 0, 0, '2', 0, 0, 0, '6', 0, '4', 0, 0, 0, '8', 0, 0, 0, 0, '3', '2', 0, '7']
ar = []
var1 = [9, 2, 3, 5, 4, 7, 8, 6, 1, 3, 1, 2, 7, 8, 6, 9, 4, 5, 7, 6, 5, 1, 2, 9, 3, 8, 4, 2, 8, 4, 3, 1, 5, 7, 9, 6, 4, 3, 1, 9, 6, 2, 5, 7, 8, 1, 4, 7, 2, 9, 8, 6, 5, 3, 6, 5, 9, 8, 7, 1, 4, 3, 2, 5, 7, 8, 6, 3, 4, 1, 2, 9, 8, 9, 6, 4, 5, 3, 2, 1, 7]
for i in array:
    ar.append(int(i))

#print(ar)

def test(a):

    def index(i,j,k):
        return ((i)*9+j)*9+k+1

    with open("cnf.txt", "w") as f:
        count = 0
        for i in range (9):
            for j in range (9):
                if (int(a[9*i+j])>0):
                    count = count +1

        f.write ("p cnf 729 "+str(18345+count)+"\n")



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
