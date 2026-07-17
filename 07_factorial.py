#Factorial of a number
fact = 1
for i in range(1,6):
    fact *=i
print("factorial of a number:",fact)

# taking input from the user
fact = 1
start = int(input("enter a starting number:"))
end = int(input("enter a ending number:"))
for i in range(start,end+1):
    fact *= i
print("factorial of a number:",fact)