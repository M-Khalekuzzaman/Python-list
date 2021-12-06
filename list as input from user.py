'''
n = input("Enter a text of number :")
list = n.split()
sum = 0
for num in list :
    sum = sum +int(num)
print("total sum is = ",sum)
'''
text = input("Enter a text of number :")

numOfWords = 0
numOfLetters = 0
numOfDigits = 0
for x in text :
    if x >= 'a' and x<='z':
        x = x.lower()
        numOfLetters = numOfLetters + 1
    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1
    elif x ==' ':
        numOfWords = numOfWords + 1

print(numOfWords + 1)
print(numOfDigits)
print(numOfLetters)