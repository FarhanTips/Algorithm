

import heapq

def solve(graph,source):

    visited = [0] * len(graph)
    dist = [-1] * len(graph)
    dist[source - 1] = 0
    queue = []
    queue.append([0,source])

    while len(queue)>0:
        heapq._heapify_max(queue)
        u,v = queue.pop(0)
        for i, j in graph[v]:
            if dist[i - 1] == -1:
                dist[i - 1] = j
                queue.append((dist[i - 1], i))

            alter= min(j, dist[v - 1])
            if alter > dist[i - 1]:
                queue.append((dist[i - 1], i))
                dist[i - 1]=alter

    return dist

fdata=open('C:\\Users\\User\\Pictures\\input5.txt', 'r')
data = fdata.read()
data= data.split('\n')

out=open("C:\\Users\\User\\Pictures\\output5.txt", 'w')

number_of_graphs = int(data.pop(0))
for x in range(number_of_graphs):
    graph = {}
    nodes, edges = data[0].split()
    data=data[1:]

    for i in range(1, int(nodes) + 1):
        graph[i]=[]

    for j in range(int(edges)):
        u, v, w =data[0].split()
        data=data[1:]
        graph[int(u)].append([int(v), int(w)])

    source=int(data[0])
    data=data[1:]
    print(graph)

    outcome = solve(graph,source)
    for i in outcome:
        out.writelines(f"{i} ")
    out.writelines(f"\n")
    print(outcome)


#files close
fdata.close()
out.close()