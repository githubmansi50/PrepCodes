#Day 1:
#Program to Find Greatest of Two Numbers


firstNum = int(input("Enter First Number: "))
secondNum = int(input("Enter Second Number: "))

if firstNum > secondNum:
    print(firstNum, "greater than", secondNum)
    
elif secondNum < firstNum:
    print(secondNum, "greater than", firstNum)

else:
    print("Both are equal")
