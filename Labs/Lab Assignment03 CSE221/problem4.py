
def shortest_path(dict,source,endpoint):
    find = ""
    result = 0
    for i in range(len(dict)):
        for i in dict:
            for x in dict[i]:
                if find == "":
                    if x == endpoint:
                        find = i
                        result += 1

        count = -1
        for i in dict:
            count += 1
            if i == find:
                break
        xu = ""
        for i in range(count - 1, -1, -1):
            for x in dict:
                if find in dict[x]:
                    xu += x
                    result += 1
                    find = x
                    break
            if xu != "":
                break

        if source == xu:
            break
    return result

vu=""
#input file open
fdata=open("C:\\Users\\User\\Pictures\\input4.txt","r")
fdata=fdata.readlines()
data=fdata[1:]

num_of_graphs=int(fdata[0])

for g in range(num_of_graphs):
    bi=(data[0])
    total_places=int(bi[0])
    data=data[1:]
    moto=data[0:int(bi[2])]
    ck=moto[0]
    source=ck[0]

    # create Dictionary for graph
    graph = {}
    for i in range(1, total_places + 1):
        graph[str(i)] = []

    edge = []
    for i in moto:
        i = i.split()
        edge.append(i)
    for i, j in edge:
        graph[i].append(j)


    outcome = shortest_path(graph, source, bi[0])


    vu=vu+f"{outcome}\n"
    data=data[int(bi[2]):]
# output file open
output = open("C:\\Users\\User\\Pictures\\output4.txt", "w")
output.writelines(f"{vu}")