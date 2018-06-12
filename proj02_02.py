# Name:
# Date:

# project02_02: Fibonacci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the
sequence. The sequence looks like this:
1, 1, 2, 4, 7, 8, etc... """

times = int(raw_input("how many fibonacci numbers do you want?"))

Previous = 0
Current = 1
Next = int(Previous+Current)

for Next in range(1, times + 1):
    print Current
    Next = int(Previous + Current)
    Previous = Current
    Current = Next













