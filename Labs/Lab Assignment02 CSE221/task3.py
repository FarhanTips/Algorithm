

def Insertion_sort(A):
    for i in range(len(A)):
        for j in range(i-1,-1,-1):
            if A[j]<A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
            else:
                break

#input2 file open
fdata=open("C:\\Users\\User\\Pictures\\input3.txt","r")
size,id,marks=fdata.readlines()

size=size.split()
id=id.split()
marks=marks.split()

list=[]

for i in range(int(size[0])):
    list.append([int(marks[i]), int(id[i])])

a=Insertion_sort(list)

#Output2 file open
output=open("C:\\Users\\User\\Pictures\\output3.txt","w")

for i in list:
    output.writelines(f"{i[1]} ")

#All file close
fdata.close()
output.close()
