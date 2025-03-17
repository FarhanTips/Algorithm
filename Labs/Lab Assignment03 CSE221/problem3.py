

def DFS_VISIT(graph,source,place,visited,printed,endpoint):

    visited[int(source) - 1] = 1
    printed.append(source)
    printed.append(" ")

    for each_source in graph[source]:
        if visited[int(each_source) - 1] == 0 and (endpoint not in printed):
            DFS_VISIT(graph,each_source,place,visited,printed,endpoint)

def DFS(graph,endpoint,place,printed):
    visited = [0] * place
    for i in graph:
        if visited[int(i) - 1] == 0 and (endpoint not in printed):
            DFS_VISIT(graph,i,place,visited,printed,endpoint)

    for i in printed:
        print(i,end="")

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input3.txt","r")
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

printed=[]
DFS(graph,"12",total_places,printed)

#output file open
output=open("C:\\Users\\User\\Pictures\\output3.txt","w")
output.writelines(printed)
