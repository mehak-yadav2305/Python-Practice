#print odd numbers from 1 to 1000
for i in range(1,1000,2):
    print(i)
#print odd numbers between 1121 to 2456
for i in range(1121,2456,2):
    print(i)


#print total number of odd number between 111 to 211
total=0
for i in range(111,211,2):
    total += 1
print("total number of odd numbers",total)

#taking input from the user
start = int(input("enter a starting number:"))
end = int(input("enter the ending number:"))
for i in range(start,end+1):
    if i%2!=0:
        print(i)