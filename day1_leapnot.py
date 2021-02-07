#Day 1:
#Python Program to Check Leap Year or Not
year = int(input("Enter a Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
           print("No, {} is not a Leap Year".format(year))
    else:
        print("No, {} is not a Leap Year".format(year))
else:
    print("No, {} is not a Leap Year".format(year))    