#Day 2:
#Python Program to find the Reverse of a given number

#Step 1. Take the user number for variable num.
#Step 2. Take a temp variable and initialized with num value.
#Step 3. Take reverse variable and initialized with 0. 
#Step 4. Run a while until num > 0. 
#Step 5. Then inside while loop, Obtain remainder.
#Step 6. Multiply the reverse variable with 10 and add the obtained remainder to it.
#Step 7. Now, divide num by 10 and stored it again in num variable.
#Step 8. Repeat Step 5,6,7 until while loop condition gets false.
#Step 9, Now print the reverse number as output.
#Step 10. Stop.


num = int(input("Enter a Number: "))
temp = num
reverse = 0

while num>0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print("The given number is : {} ".format(temp))
print("The reversed number is : {} ".format(reverse))