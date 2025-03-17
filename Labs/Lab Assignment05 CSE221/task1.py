
def Maximum_assignments(list):
    list=sorted(list, key=lambda l: l[1])
    finish=0
    new=[]
    for i in list:
        if finish<=i[0]:
            new.append(i)
            finish=i[1]
    return new

fdata=open("C:\\Users\\User\\Pictures\\input1.txt","r")
data=fdata.readlines()

outcome=open("C:\\Users\\User\\Pictures\\output1.txt","w")
while len(data)>0:
    list = []
    N=int(data[0])
    data=data[1:]
    for i in range(N):
        S,E=data[0].split()
        list.append([int(S),int(E)])
        data=data[1:]

    result=Maximum_assignments(list)
    print(result)
    outcome.writelines(f"{len(result)}\n")
    for i,j in result:
        outcome.writelines(f"{i} {j}\n")

#All files Close
fdata.close()
outcome.close()