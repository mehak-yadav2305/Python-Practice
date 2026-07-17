# print numbers from 1500 to 2000 in reverse order
#for i in range(2000,1500,-1):
   # print(i)

#print even numbers in reverse order
#for i in range(200,100,-2):
   # print(i)
 
#print odd numbers taking input from users
n=int(input("enter a number:"))
     #if n is even , make it odd
if n %2 ==0:
    n=n-1
for i in range(n,1,-2):
    print(i)