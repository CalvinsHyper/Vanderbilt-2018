# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!
print "Hello"
Your_Name = raw_input("What's your name?")
print "Your name is "+ Your_Name
Your_Grade = raw_input("What Grade are you in?")
print "you are in"+ Your_Grade
x = 16-int(Your_Grade)
print "you wil graduate in" +str(x) +  "Years"

print "Part II"
Current_Month = raw_input("what is the current month NUMBER")
Current_Day = raw_input("What is the current day NUMBER")
Your_Month = raw_input("what is your birth month NUMBER?")
Your_Day = raw_input("what day of the month is your Birthday NUMBER?")
q= Your_Month-Current_Month
w=12-(Current_Month-Your_Month)
e=Your_Day-Current_Day
r=30-(Current_Day-Your_Day)
if Your_Month>Current_Month:
    print "the number of months until your bday is " +str( q)
else:
    print"the number of months until your bday is "  +str( w)

if Your_Day >= Current_Day:
    print "the number of days until your bday is"  +str(e)

else:
    print "The number of days until your birthday is" +str(r)









