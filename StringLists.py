#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)
user_string = str(input("Enter a string:"))
if (user_string == user_string[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    