"""
Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.

Enter your name: Chuck
Hello Chuck
"""
name = input('Enter your name: ')
print('Hello ', name)


"""
Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
"""
hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

# use numbers only
try:
    fhrs = float(hrs)
    frate = float(rate)
except:
    print('Please, use numbers')

# getting the total pay
pay = frate*fhrs

# print the total payment
print("Pay: ", pay)

"""
Exercise 4: Assume that we execute the following assignment statements:

width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the type 
(of the value of the expression).

    width//2    8

    width/2.0   8.5

    height/3    5.666667

    1 + 2 * 5   11

"""

"""
Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.
"""

cels = input('Enter Celsius temperature: ')

# converting to float
try:
    fcels = float(cels)
except:
    print("Please, only use numbers.")

# converting to fahrenheit
ftemp = (fcels * 9/5) + 32

# print the result
print(ftemp, '°F')