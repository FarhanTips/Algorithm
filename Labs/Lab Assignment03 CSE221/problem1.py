
#input file open
fdata=open("C:\\Users\\User\\Pictures\\input1.txt","r")
fdata=fdata.readlines()
data=fdata[2:]

total_places=int(fdata[0])
total_connections=int(fdata[1])

#create Dictionary for graph
graph={}
for i in range(1,total_places+1):
    graph[str(i)]=[]

edge=[]
for i in data:
    i=i.split()
    edge.append(i)

for i,j in edge:
    graph[i].append(j)

result=f"{total_places}\n"
for i in graph:
    result+=f"{i}  "
    for j in graph[i]:
        result+=f"{j}  "
    result+="\n"

#output file open
output=open("C:\\Users\\User\\Pictures\\output1.txt","w")
output.writelines(result)

