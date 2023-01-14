"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times 
the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

# converting
try:
    fhrs = float(hrs)
    frate = float(rate)
except:
    print('Please, use only numbers')
    quit()

# calculating the extra
if fhrs > 40:
    xtra = (fhrs - 40) * (frate * 1.5)
    total = (40 * frate) + xtra
else:
    total = frate * fhrs

print('Pay: ', total)


"""
Exercise 2: Rewrite your pay program using try and except so that your program handles
non-numeric input gracefully by printing a message and exiting the program. 
The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""

# It's actually what I've been doing before, so I'm going to skip this one

"""
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error message. 
If the score is between 0.0 and 1.0, print a grade using the following table:

 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various different values for input.
"""
score = input('Enter score: ')

try:
    fscore = float(score)
except:
    print('Bad score. Try using numbers betweet 0.0 and 1.0')
    quit()

if fscore > 1.0:
    print('1.0 is the maximum. Please try again')
    quit()

if fscore >= 0.9 and fscore <= 1.0:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
elif fscore < 0.6:
    print('F')