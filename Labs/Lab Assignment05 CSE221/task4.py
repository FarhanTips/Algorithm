
def Check_integer(a,b):
    new=[]
    count=0
    for i in range(a,b+1):
        if type(i ** 2) == int:
            test = i ** 0.5
            test = int(test)
            if test ** 2 ==i:
                new.append(i)
                count+=1
    print(new)
    return count

fdata=open("C:\\Users\\User\Pictures\\input4.txt","r")
data=fdata.readlines()

outcome=open("C:\\Users\\User\Pictures\\output4.txt","w")

while len(data)>0:
    a,b=data[0].split()
    if a=="0" and b=="0":
        data=data[1:]
    else:
        data=data[1:]
        result=Check_integer(int(a),int(b))
        outcome.writelines(f"{result}\n")

#All files close
fdata.close()
outcome.close()