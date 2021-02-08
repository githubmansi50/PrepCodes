#Day 2:
#Python program to find Fibonacci series up to n

#Step 1. Start
#Step 2. Take a user input and store into int type num variable.
#Step 3. Initialize n1, n2 variable to 0, 1.
#Step 4. Run a for loop starts from 2 to num value.
#Step 5. Inside for loop, using arithmetic addition method, and calculate the n3, where n3 = n1 + n2. Then initialize n1 = n2 and n2 = n3.
#Step 6. Print n3 inside the loop.
#Stop 7. Stop

num = int(input("Enter a number: "))
n1 = 0
n2 = 1

print("Fibonacci Series: ", n1, n2, end = " ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = " ")
print()