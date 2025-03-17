

def BFS(result,graph,source,endpoint,place):
    visited=[0]*place
    queue=[]
    visited[int(source)-1]=1
    queue.append(source)

    while len(queue)>0:
        m=queue.pop(0)
        result+=f"{m} "
        if m==endpoint:
            break
        for i in graph[m]:
            if visited[int(i)-1]==0:
                visited[int(i)-1]=1
                queue.append(i)
    return result

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input2.txt","r")
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

result=""
outcome=BFS(result,graph,"1","12",total_places)

#output file open
output=open("C:\\Users\\User\\Pictures\\output2.txt","w")
output.writelines(outcome)

