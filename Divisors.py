#Create a program that asks the user for a 
#number and then prints out a list of all the divisors of that number.

input_number = int(input("Find divisors for this number:"))
divisor_list = []
for i in range(1, input_number + 1):
    if input_number % i == 0:
        divisor_list.append(i)
print(divisor_list) 