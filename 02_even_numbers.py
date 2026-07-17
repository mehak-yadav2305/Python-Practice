for i in range(2,21,2):
   print(i)

# print total number of even numbers occur between 1 - 200
count = 0
for i in range(1,200):
    if i%2==0:
        print(i)
        count +=1
print("Total even number",count)

#taking input from user
start = int(input("enter a starting number:"))
end = int(input("enter the ending number:"))
for i in range(start,end+1):
    if i%2==0:
        print(i)
