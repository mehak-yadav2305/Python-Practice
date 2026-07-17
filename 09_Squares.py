#Square of numbers
n=int(input("enter a number:"))
c = n*n
print("square of",n,":",c)

# squares of multiple number (for loop)
for i in range(1,6):
    c=i*i
    print("square of",i,":",c)

#taking input from user(for loop)
start = int(input("enter a starting number:"))
end = int(input("enter a ending number:"))
for i in range(start,end+1):
    c=i*i
    print("square of",i,":",c)
