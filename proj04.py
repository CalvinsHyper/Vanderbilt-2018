# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

d

"""
#Part I
#Take a list, say for example this one:
#and write a program that prints out all the elements of the list that are less than 5

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]





#Part II
# Take two lists, say for example these two:
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in b:
    for item_c in c:
        if item == item_c:
            print item

#Part III
# Take a list, say for example this one:
# and write a program that replaces all “a” with “*”.

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]

for item_d in d:
    if item_d == "a":
        print "*"
    elif item_d != "a":
        print item_d

#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

number = str(raw_input("what word would you like to palindrome test?"))
for item in number:
    if number[0] != number[-1]:
        print "It is not a palindrome"
        break
    elif number[-1] == number[0]:
        print "it is a palindrome"
        break










