#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Enter your name:")
age = int(input("Enter your age:"))

year100 = 100 - age
print("In {} years you will be hundred years old".format(year100))