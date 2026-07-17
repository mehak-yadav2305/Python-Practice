#Count Digits in a number (using while loop)
num=509
count = 0
while num>0:
    count += 1
    num=num//10
print("Total digit:",count)

#using for loop
num = input("enter a number:")
count = 0
for i in str(num):
    count += 1
print("Total digits:",count)