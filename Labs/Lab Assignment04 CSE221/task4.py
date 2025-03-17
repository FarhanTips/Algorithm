

import heapq

def Dijkstra(graph,source):
    dist = [float('infinity')] * len(graph)
    dist[source-1]=0
    queue=[]
    queue.append([0,source])
    visited = [0] * len(graph)

    connections = []
    for i in range(len(graph)):
        connections.append([])

    while len(queue) != 0:
        connections[source - 1].append(source)
        heapq.heapify(queue)

        u,v = queue.pop(0)
        for i, j in graph[v]:
            if visited[i - 1]:
                continue
            if dist[i - 1] > j + u:
                connections[i - 1] = connections[v - 1] + [i]
                dist[i - 1] = j + u
                queue.append([dist[i - 1], i])

    return connections[len(graph) - 1]


#open input1
fdata=open("C:\\Users\\User\\Pictures\\input2.txt", 'r')
data = fdata.readlines()
print(data)
#open output1
out=open("C:\\Users\\User\\Pictures\\output2.txt","w")

v,e=data[0].split()

bi=data[1].split()

graph={1:[]}
for i in range(int(v)-2):
  graph[(65+i)]=[]
#print(graph)
for j in data[1:]:
    x=j.split()
    u,v,w=x
    if u=="Motijheel":
        print(v)
        graph[int(1)].append([int(ord(v)), int(w)])
    if v=="MOGHBAZAR":
        graph[int(ord(u))].append([int(2), int(w)])

    if u!="Motijheel" and v!="MOGHBAZAR":
        graph[int(ord(u))].append([int(ord(v)), int(w)])

    outcome= Dijkstra(graph, 1)
    for i in outcome:
        out.writelines(f"{i} ")
    out.writelines(f"\n")
    print(outcome)

print(graph)



#files close
fdata.close()
out.close()