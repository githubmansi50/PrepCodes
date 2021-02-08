#Day 2:
#Python Program to Find a Number is Palindrome or not

#Step 1. Take the user number for variable number.
#Step 2. Take a temp variable and initialized with number value.
#Step 3. Take reverse variable and initialized with 0. 
#Step 4. Run a while until number > 0. 
#Step 5. Then inside while loop, Obtain remainder.
#Step 6. Multiply the reverse variable with 10 and add the obtained remainder to it.
#Step 7. Now, divide number by 10 and stored it again in number variable.
#Step 8. Repeat Step 5,6,7 until while loop condition gets false.
#Step 9, Now, Outside the while loop Check temp == reverse. If this condition is true, then print, “Given number is Palindrome”.
#Step 10. Else, Print, “Given number is not Palindrome”. 
#Step 11. Stop.


num = int(input("Enter a Number: "))
temp = num
reverse = 0

while num>0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

if temp == reverse:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
