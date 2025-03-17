
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

#open output1
out=open("C:\\Users\\User\\Pictures\\output2.txt","w")

number_of_graphs = int(data.pop(0))
for x in range(number_of_graphs):
    graph = {}
    nodes, edges = data[0].split()
    data=data[1:]

    for i in range(1, int(nodes) + 1):
        graph[i] = []

    for j in range(int(edges)):
        u, v, w =data[0].split()
        data=data[1:]
        graph[int(u)].append([int(v), int(w)])

    outcome= Dijkstra(graph, 1)
    for i in outcome:
        out.writelines(f"{i} ")
    out.writelines(f"\n")
    print(outcome)

#files close
fdata.close()
out.close()
