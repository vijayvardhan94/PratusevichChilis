#Take a list, say for example this one:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

alist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for i in alist:
    if i < 5:
        newlist.append(i)
print(newlist)
#keep indentation in mind


