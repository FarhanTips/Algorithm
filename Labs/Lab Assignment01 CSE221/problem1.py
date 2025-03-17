
def isPalindrome(input_word):
    if len(input_word)==0:
        return "not palindrome"
    elif input_word!=input_word[::-1]:
        return "not palindrome"

    return "palindrome"


#input file open
fdata=open('C:\\Users\\User\\Pictures\\input.txt',"r")
data=fdata.readlines()

even_parity=0
odd_parity=0
no_parity=0
palindrome=0
no_palindrome=0

#Output file Open
output=open("C:\\Users\\User\\Pictures\\output.txt","w")

for i in data:
    number, word = i.split()
    connect=""

    #Parity Checker
    if int(float(number))!=float(number):
        connect=f"{number} cannot have parity"
        no_parity+=1
    elif int(number)%2==0:
        connect=f"{number} has even parity"
        even_parity+=1
    else:
        connect=f"{number} has odd parity"
        odd_parity+=1

    #Palindrome Checker
    test = isPalindrome(word)
    if test=="palindrome":
        connect+=f" and {word} is a palindrome"
        palindrome+=1
    else:
        connect+=f" and {word} is not a palindrome"
        no_palindrome+=1

    output.writelines(f"{connect}\n")

total_input=even_parity+odd_parity+no_parity

odd=f"Percentage of odd parity: {int((odd_parity/total_input)*100)}%\n"
even=f"Percentage of odd parity: {int((even_parity/total_input)*100)}%\n"
no=f"Percentage of odd parity: {int((no_parity/total_input)*100)}%\n"
pal=f"Percentage of palindrome: {int((palindrome/total_input)*100)}%\n"
no_pal=f"Percentage of non-palindrome: {int((no_palindrome/total_input)*100)}%"

#record file Open
record=open("C:\\Users\\User\\Pictures\\record.txt","w")

record.writelines(odd)
record.writelines(even)
record.writelines(no)
record.writelines(pal)
record.writelines(no_pal)

#All files close
fdata.close()
output.close()
record.close()


