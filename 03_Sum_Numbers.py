# Sum of numbers from 1 t0 100
total=0
for i in range(1,101):
    total += i
print ("Sum",total)


# Sum of Even Numbers from 1 to 200
total=0
for i in range(2,201,2):
    total += i
print ("Sum",total)

#taking input from the user
total = 0
start=int(input("enter a starting number:"))
end=int(input("enter a ending number:"))
for i in range(start,end+1):
    total += i
print("Sum:",total)
