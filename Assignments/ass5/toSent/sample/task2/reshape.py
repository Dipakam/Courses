import string
file = open('callgraph.txt','r')
#fileline = file.split('\n')
array = []
for i in file:
    i=i.split()
    if(i==[] or i[0]=='Call'or i[0]=='granularity:' or i[0]=='index' or i[0]=='Index'):
        continue
    else:
        array.append(i)
#    print(i)
#print(array)
Array = []
Array.append([])
j=0
for i in array:
    if(i==['-----------------------------------------------']):
        Array.append([])
        j = j+1
    else:
        #print(i)
        Array[j].append(i)
h=1
finalarray = []
k=0

for i in Array:
    for j in i:
        finalarray.append(j)
        if(j[0]==j[-1] and len(j)>1):
            break
Len = len(finalarray)
Finalarray = []


l=0
while (l<Len-1):
    temp = []
    if(len(finalarray[l])== 1):
        l=l+1
        continue
    if(l % 2 == 0):
        #print(finalarray[l][-2])
        temp.append(finalarray[l][-2])
        temp.append(finalarray[l][0])
        temp.append(finalarray[l+1][-2])
        temp.append(finalarray[l+1][2])
        Finalarray.append(temp)
    l=l+1

for i in Finalarray:
    print(i[0],i[1],i[2],i[3],sep=',',end='\n')
#for i in Array:
#    print(i)
