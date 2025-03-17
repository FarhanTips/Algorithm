

def Selection_sort(A):
    max_idx=0
    max=int(A[0])
    for i in range(len(A)-1,-1,-1):
        max_idx=i
        max=int(A[i])
        for j in range(0,i):
            if int(A[j])>max:
                max=int(A[j])
                max_idx=j
        temp=int(A[max_idx])
        A[max_idx]=int(A[i])
        A[i]=temp

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input1.txt","r")
data,list=fdata.readlines()
d=data.split()
l=list.split()

p=Selection_sort(l)

#output file open
output=open("C:\\Users\\User\\Pictures\\output1.txt","w")
for i in range(int(d[1])):
    output.writelines(f"{l[i]} ")

#All files close
fdata.close()
output.close()