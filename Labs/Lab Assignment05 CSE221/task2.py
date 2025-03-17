
def Maximum_assignments(list):
    N,M=list[0]
    list=list[1:]
    list=sorted(list, key=lambda l: l[1])
    new=[]
    count=0
    for j in range(M):
        finish = 0
        for i in list:
            if finish<=i[0] and i not in new:
                new.append(i)
                finish=i[1]
                count+=1
    return count

fdata=open("C:\\Users\\User\\Pictures\\input2.txt","r")
data=fdata.readlines()

outcome=open("C:\\Users\\User\\Pictures\\output2.txt","w")
while len(data)>0:
    list = []
    N,M=data[0].split()
    list.append([int(N),int(M)])
    data=data[1:]
    for i in range(int(N)):
        S,E=data[0].split()
        list.append([int(S),int(E)])
        data=data[1:]

    result=Maximum_assignments(list)
    print(result)
    outcome.writelines(f"{result}\n")

#All files Close
fdata.close()
outcome.close()
