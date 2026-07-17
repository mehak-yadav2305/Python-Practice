#reversing a number (using while loop)
num = int(input("enter a number:"))
reverse = 0
while num > 0:
    last_digit = num%10
    reverse = reverse*10 +last_digit
    num = num//10
print("Reversed number:",reverse)

#reversing a number(using for loop)
num = int(input("enter a number:"))
reverse = 0
for i in str(num):
    last_digit = num%10
    reverse = reverse*10 + last_digit
    num = num//10
print("Reversed number:",reverse)

# using string slicing
num = input("enter a number:")
print("Reversed number:",num[::-1])