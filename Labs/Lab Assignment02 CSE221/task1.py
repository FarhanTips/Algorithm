
def Bubble_sort(array):
    test=False
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if int(array[j]) > int(array[j + 1]):
                temp=int(array[j+1])
                array[j + 1]= int(array[j])
                array[j]=temp

                test=True

        if test==False:  
            break
    return array

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input1.txt","r")
data,list=fdata.readlines()
l=list.split()
p=Bubble_sort(l)

#output file open
output=open("C:\\Users\\User\\Pictures\\output1.txt","w")
for i in range(int(data)):
    output.writelines(f"{l[i]} ")

#All files close
fdata.close()
output.close()