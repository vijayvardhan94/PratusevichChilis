#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Enter a number:"))
if number % 2 == 0 and number % 4 == 0:
    print("This is divisible by 4!")
elif number % 2 == 0:
    print("The number is even")
else: 
    print("The number is odd!")

    
