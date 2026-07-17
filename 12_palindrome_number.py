# check palindrome number(using while loop)
num = 1221
original = num
reverse = 0
while num>0:
    last_digit = num % 10
    reverse = reverse*10 + last_digit
    num = num//10
if reverse == original:
    print(original,"is a palindrome number")
else:
    print(original,"is not a palindrome number")

#using for loop
num = int(input("enter a number:"))
original = num
reverse = 0
for i in str(num):
    last_digit = num % 10
    reverse = reverse*10 + last_digit
    num = num//10
if original == num:
    print(original,"is a palindrome number")
else:
    print(original,"is not a palindrome number")