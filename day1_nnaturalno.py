#Day 1:
#Python Program to Find the Sum of First N Natural Numbers

#Step 1. Start
#Step 2. Initialize the value variable to 0.
#Step 3. Take a one input from the user and store it into variable num.
#Step 4. Start a for loop from range starts from 1 to num +1 .
#Step 5. In for loop for every cycle value will be incremented by i.
#Step 6.When condition gets false print value.
#Step 7. Stop 

# i.e. -> input - 8 | 1+2+3+4+5+6+7+8 = 36

num = int(input("Enter a Number:"))
val = 0
for i in range(1, num+1):
    val = val + i
print("Sum of n natural numbers: ",val)