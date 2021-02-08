#Day 2:
#Python Program to find the Factorial of a number

#Step 1.Read the number num.
#Step 2.Initialize the variable factorial=1
#Step 3.To take a user input for factorial of number
#Step 4.We use for loop starts from 1 to num + 1.
#Step 5.Then, Inside For loop factorial = factorial * i
#Step 6.Print the variable of factorial.
#Step 7.Stop



num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i    
print("Factorial of the Number: ",fact)