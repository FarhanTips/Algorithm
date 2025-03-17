
def LCS(X,Y):
    m = len(X)
    n = len(Y)

    c=[]
    for i in range(m+1):
        test=[]
        for j in range(n+1):
            test.append(0)
        c.append(test)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                maximum_up_left = max(c[i - 1][j], c[i][j - 1])
                c[i][j] = maximum_up_left

    string = ""
    j = m
    k = n
    while j > 0 and k > 0:
        if X[j - 1] == Y[k - 1]:
            string = X[j - 1] + string
            j -= 1
            k -= 1
        elif c[j - 1][k] > c[j][k - 1]:
            j -= 1
        else:
            k -= 1
    print(f"Longest Common Subsequence's initial: {string}")
    return string, c[m][n]


dict= {"Y":"Yasnaya","R": "Rozhok","S":"School","P":"Pochinki","F":"Farm","M":"Mylta","H":"Shelter","I":"Prison"}

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input2.txt", 'r')
data=fdata.readlines()

number_of_zones = int(data[0])
actual_zones = data[1].split()
actual_zones = actual_zones[0]

prediction_zones = data[2].split()
prediction_zones = prediction_zones[0]

lcs_string, length = LCS(actual_zones,prediction_zones)

Correctness = (length/number_of_zones) * 100

#output file open
outcome= open('C:\\Users\\User\\Pictures\\output2.txt', 'w')

for i in lcs_string:
    outcome.write(f'{dict[i]} ')

outcome.write(f'\nCorrectness of prediction: {int(Correctness)}%')


#All files close
fdata.close()
outcome.close()

