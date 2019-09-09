fo = open('input.txt','r')
cont = fo.read()
lines = cont.split('\n')
firstRow = lines[0].split(' ')
literals = int(firstRow[2])
clauses = int(firstRow[3])
#print(literals)
#print(clauses)
Clause = []
for x in range(1,clauses+1):
    #print(x)
    row = lines[x]
    intLit = []
    literalRow = row.split(' ')
    for n in literalRow:
        intLit.append(int(n))
    intLit.pop()
    Clause.append(intLit)

newClause = []
newLiteral = []
def unit(newClause,newLiteral):
    print(newClause)
    print(newLiteral)
    newClause1 = []
    arra = []
    for i in newClause:
        for j in i:
            arra.append(j)
        newClause1.append(arra)
        arra = []
    #CountUnits = 0
    for news in newClause1:
        if(len(news)==0):
            return 0

    if(len(newClause1)==0):
        return 1

    for news in newClause1:
        if (len(news)==1):
            #CountUnits = CountUnits +1
            newLiteral.append(news[0])

    for x in newLiteral:
        for y in newLiteral:
            if(x+y==0):
                return 0

    for chad in newClause1[0]:
        for alpha in newLiteral:
            if (chad+alpha==0):
                continue
        newLiteral.append(chad)
        """for n in range(0,len(newClause1)):
            print(n)
            for m in newLiteral:
                print(m)
                print(newClause1)
                if m in newClause1[n]:
                    newClause1.pop(n)
                neg = (-1)*m
                if neg in newClause1:
                    newClause1[n].remove(neg)"""
        for m in newLiteral:
            for n in newClause1:
                if m in n:
                    newClause1.remove(n)
            for n in newClause1:
                neg = (-1)*m
                if neg in n:
                    n.remove(neg)

        #print(newClause1)

        #print(chad)
        if(unit(newClause1,newLiteral)==1):
            return 1
        else:
            #print(Main)

            newClause1 = []
            are = []
            for i in Main:
                for j in i:
                    are.append(j)
                newClause1.append(are)
                are = []


            fakelit = []
            c = 0
            for i in newLiteral:
                if(i == chad):
                    c = 1
                    #print('Here it goes')
                if(c == 0):
                    fakelit.append(i)
                    #print(fakelit)

                    #print('this was done')

            newLiteral = []
            for j in fakelit:
                newLiteral.append(j)

            #print(newLiteral)
            #print('finally you got this')
            #newLiteral.remove(chad)
            #newClause1 = Clause.copy()
            #print(newClause1)
            #print('hi')
    return 0
Main = []
arre = []
for i in Clause:
    for j in i:
        arre.append(j)
    Main.append(arre)
    arre = []
Clause1 = Clause.copy()
print(unit(Clause1,[]))
