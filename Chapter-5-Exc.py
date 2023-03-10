"""
Exercise 1: Write a program which repeatedly reads numbers 
until the user enters “done”. Once “done” is entered, 
print out the total, count, and average of the numbers. 
If the user enters anything other than a number, 
detect their mistake using try and except and print an error 
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""
num = 0
total = 0.0

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    
    try:
        fnumber = float(x)
    except:
        print('Invalid input')
    
    num = num + 1
    total = total + fnumber

print (total, num, total/num)

"""
Exercise 2: Write another program that prompts for a list of numbers as above and at the end 
prints out both the maximum and minimum of the numbers instead of the average.
"""
maxi = 0
mini = 0

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    
    try:
        fnumber = int(x)
    except:
        print('Invalid input')
    
    if fnumber > maxi:
        maxi = fnumber
    if mini == 0:
        mini = fnumber
    if fnumber < mini:
        mini = fnumber
    
print(maxi, mini)