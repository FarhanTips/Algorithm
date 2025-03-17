
fdata=open("C:\\Users\\User\\Pictures\\input3.txt","r")
data=fdata.readlines()

N=int(data[0])
c=data[2]

temp=data[1]
time=[]
temp=(temp.split())
for i in temp:
    time.append(int(i))

time=sorted(time)
sequence_of_tasks=[]
jack_hour=0
jill_hour=0
jack_task = []
jill_task=[]

for i in c:
    if i=="J":
        a=time.pop(0)
        jack_task.append(a)
        sequence_of_tasks.append(a)
        jack_hour+=a

    elif i=="j":
        jack_task=sorted(jack_task,reverse=True)
        b=jack_task.pop(0)
        jill_task.append(b)
        sequence_of_tasks.append(b)
        jill_hour+=b

outcome=open("C:\\Users\\User\\Pictures\\output3.txt","w")
for i in sequence_of_tasks:
    outcome.writelines(f"{i}")
outcome.writelines(f"\nJack will work for {jack_hour} hours\n")
outcome.writelines(f"Jill will work for {jill_hour} hours")
