#Ask the user for a number and return a list that contains only elements 
#from the original list a that are smaller than that number given by the user.


lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 

base = int(input("Enter a base number; numbers from list will be below this:"))
new_list = [x for x in lst if x < base]
print(new_list)