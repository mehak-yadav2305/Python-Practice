#Product of numbers from 1 to 5
product = 1
for i in range(1,6):
    product *= i
print("product of numbers:",product)

# taking input from the user
product = 1
start = int(input("entera starting number:"))
end = int(input("enter a ending number:"))
for i in range(start,end+1):
    product *= i
print("product of numbers:",product)