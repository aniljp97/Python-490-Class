# float numbers are created from division of integers if its not whole
# python 3 requires parentheses around for print statements unlike 2
# Python 3 has distinct str and byte type variables
# Python 3 has no xrange function

str1 = input("Enter: ")
str1 = str1.replace('python', 'pythons')
print(str1)

num1 = int(input("Enter number: "))
num = num1
as_num = 0
while num > 1:
    as_num = as_num + int(num % 10)**3
    num = num / 10

if as_num == num1:
    print(num1, "is Armstrong")
else:
    print(num1, "is NOT Armstrong")


str2 = input("Enter: ")
if str2[::-1] == str2:
    print("It is a palindrome")
else:
    print("Is NOT a palindrome")