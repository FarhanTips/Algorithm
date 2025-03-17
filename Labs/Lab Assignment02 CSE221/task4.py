
def Merge_sort(array):
    if len(array)>=2:
        left = array[:len(array)//2]
        right = array[len(array)//2:]

        Merge_sort(left)
        Merge_sort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if int(left[i]) < int(right[j]):
                array[k] = int(left[i])
                i += 1
            else:
                array[k] = int(right[j])
                j += 1
            k += 1

        while j < len(right):
            array[k] = int(right[j])
            j += 1
            k += 1

        while i < len(left):
            array[k] = int(left[i])
            i += 1
            k += 1

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input4.txt","r")
data,list=fdata.readlines()
l=list.split()

p=Merge_sort(l)

#output file open
output=open("C:\\Users\\User\\Pictures\\output4.txt","w")
for i in range(int(data)):
    output.writelines(f"{l[i]} ")

#All files close
fdata.close()
output.close()