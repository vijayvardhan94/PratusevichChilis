#Reverse Word Order
#Write a program (using functions!) that asks the user for a 
# long string containing multiple words. Print back to the user the same string, 
# except with the words in backwards order. For example, say I type the string:

def input_string(instring):
    a = (instring.split())
    print(a[::-1])


input_string("Hi Hello goodbye")
#convert it to 