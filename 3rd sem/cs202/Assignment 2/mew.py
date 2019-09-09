import copy
import time

tim = time.time()
fo = open('cnf.txt','r')
cont = fo.read()
lines = cont.split('\n')
firstRow = lines[0].split(' ')
literals = int(firstRow[2])
clauses = int(firstRow[3])
#print(literals)
#print(clauses)
Clause = []
Count = 0
for x in range(1,clauses+1):
    #print(x)
    row = lines[x]
    intLit = []
    literalRow = row.split(' ')
    for n in literalRow:
        intLit.append(int(n))
    intLit.pop()
    Clause.append(intLit)

#print(Clause)
p = [0 for i in range(literals)]
k = []

#lit mein all single clauses utha llo
ans =[]

for row in Clause:
    if len(row)==1 :
        k.append(row[0])

def recb(Clause1, lit):
    Count = Count +1
    todel = []
    print(lit)
    #print("enter big loop")
    print(Clause1)
    if [] in Clause1:
        Clause1.remove([])
    if len(Clause1)==0 :
        for a in lit:
            for b in lit:
                #print("hi")
                if (a+b==0):
                    return
        #print("bye")
        ans = copy.deepcopy(lit)
        print(ans)
        return -1

    x = len(Clause1[0])

    for t in range(x):
        flag = 0
        litc = copy.deepcopy(lit)
        litc.append(Clause1[0][t])
        #print(litc)

        Clause2 = copy.deepcopy(Clause1)
        #print(Clause1)

        for liti in litc:
            for row in Clause2:
                if liti in row:
                    todel.append(row)

            for de in todel:
                if de in Clause2:
                    Clause2.remove(de)
                    #print(Clause2)
                    #print("C1")
                    #print(Clause1)
            todel = []

            for row in Clause2:
                if -liti in row:
                    row.remove(-liti)
                    #print(Clause2)
                    #print("C1-")
                    #print(Clause1)
                    if len(row) == 1 and row[0] not in litc:
                        litc.append(row[0])
                        #print(litc)
            #print(Clause2)
        #print("unit propogation done for this loop")
        if [] in Clause2:
            Clause2.remove([])
        for a in litc:
            for b in litc:
                if (a+b==0):
                    flag = 1

        if flag==0:
            q = recb(copy.deepcopy(Clause2),copy.deepcopy(litc))
            if q == -1:
                return -1







if recb(copy.deepcopy(Clause),copy.deepcopy(k)) == -1:
    print ("The formula is SAT, Model is :")
    print(ans)
else:
    print ("The formula is UNSAT")

print('The total number of decompostions is ')
print(Count)
print('Time taken by the program to solve is')
print(time.time()-tim)
#ans = recb(0)
"""print(ans)
        k =n
        if k*p[abs(k)-1]<0:
            continue
        else:
            if k >0:
                p[k-1]=1
                q= recb(i+1)
                if q==-1:
                    continue
                return q
            else:
                p[-k-1]=-1
                q= recb(i+1)
                if q==-1:
                    continue
                return q
    return -1"""
