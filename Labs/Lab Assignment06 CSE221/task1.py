
def Minimum_steps(num):
    if num==0:
        return 0
    else:
        print(num, "--->", end=" ")
        list = []
        for i in range(len(str(num))):
            num2 = str(num)
            list.append(int(num2[i]))
        list2 = (sorted(list, reverse=True))
        num = num - list2[0]

        if num==0:
            print(num)

        return 1 + Minimum_steps(num)

#input1 open
fdata=open("C:\\Users\\User\\Pictures\\input1.txt","r")
data=fdata.readline()
data=int(data)

bull=Minimum_steps(data)

#output1 open
outcome=open("C:\\Users\\User\\Pictures\\output1.txt","w")
outcome.writelines(f"Minimum steps: {bull}")


#All files close
fdata.close()
outcome.close()

