
def LCS_for_3_strings(X,Y,Z):
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1

    c = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]
    t = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):

                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                    t[i][j][k] = 0

                else:
                    if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                        c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                        t[i][j][k] = c[i - 1][j - 1][k - 1]  # diagonal

                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            max = c[i - 1][j][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = c[i][j][k - 1]  # up-up-left

                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max  # max
                                t[i][j][k] = c[i][j - 1][k -1]  # left-up-up

                        else:
                            max = c[i][j - 1][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max  # max
                                t[i][j][k] = c[i - 1][j][k -1]  # up-left-up

                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max # max
                                t[i][j][k] = c[i][j - 1][k -1]  # left-up-up

    return c[m - 1][n - 1][o - 1]

#input file open
fdata=open("C:\\Users\\User\\Pictures\\input3.txt", 'r')
data=fdata.readlines()
string_1=data[0][0:-1]
string_2=data[1][0:-1]
string_3=data[2][0:]

#output file open
outcome=open("C:\\Users\\User\\Pictures\\output3.txt", 'w')

result=LCS_for_3_strings(string_1,string_2,string_3)
print(result)
outcome.write(f'{result}')


#All files close
fdata.close()
outcome.close()

