#Day 2:
#Prime or Not:

#Step 1: Intialize the variable a and count to zero
#Step 2: Read the input
#Step 3: Set a to n//2 (// in python implies integer division) , we can make a to square root of number to make it more efficient
#Step 4: iterate through 2 to a+1 and check whether it is divisible by i or not
#Step 5 : if divisible , then print “not a prime number” and set count to 1 and break from the loop
#             else continue iteration
#Step 6 : if count is still zero then the given number is prime number

a = 0
count = 0

n = int(input("Enter a number to check prime or not: "))

a = n//2  #// in python implies integer division
for i in range(2, a+1):
    if n % i == 0:
        print("It is not a prime number")
        count = 1
        break
if count == 0:
    print("It is a prime number")