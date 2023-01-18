"""
The random function is only one of many functions that handle random numbers. 
The function randint takes the parameters low and high, and returns an integer between 
low and high (including both).

>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9

To choose an element from a sequence at random, you can use choice:

>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3

The random module also provides functions to generate random values from continuous 
distributions including Gaussian, exponential, gamma, and a few more.

"""
import random
x = random.randint(5, 10)
y = random.randint(5, 10)

print(x,y)


"""
Exercise 2: Move the last line of this program to the top, so the function call 
appears before the definitions. 
Run the program and see what error message you get.

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Code: http://www.py4e.com/code3/lyrics.py
"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    
repeat_lyrics()

# Didn't really had any errors...

"""
Exercise 3: Move the function call back to the bottom and move 
the definition of print_lyrics after the definition of repeat_lyrics. 
What happens when you run this program?

Sorry Dr. Chuck, nothing really changes for me...
"""

"""
Exercise 4: What is the purpose of the “def” keyword in Python?

a) It is slang that means “the following code is really cool” (this sounds cool tho)
b) It indicates the start of a function <--
c) It indicates that the following indented section of code is to be stored for later
d) b and c are both true
e) None of the above
"""

"""
Exercise 5: What will the following Python program print out?

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()

a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC <--
e) Zap Zap Zap
"""

"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
def computepay(hours, rate):
    try:
        fhrs = float(hours)
        frate = float(rate)
    except:
        print('Please, use only numbers')
        quit()
        
    if fhrs > 40:
        total = (fhrs - 40) * (frate * 1.5) + (40 * frate)
        print(total)
    else:
        total = fhrs * frate
        print(total)
        
computepay(input('Enter Hours: '),input('Enter Rate: '))
print('Pay: ', computepay)

"""
Exercise 7: Rewrite the grade program from the previous chapter using a 
function called computegrade that takes a score as its parameter and returns a grade as a string.

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

Run the program repeatedly to test the various different values for input.
"""
def computegrade():
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
    
score = input('Enter Score: ')

try:
    fscore = float(score)
except:
    print('Bad score. Try using numbers betweet 0.0 and 1.0')
    quit()

if fscore > 1.0:
    print('1.0 is the maximum. Please try again')
    quit()

print(computegrade())
# Can't aboid to print out None