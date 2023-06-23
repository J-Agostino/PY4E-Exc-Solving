"""
Exercise 1: Write a while loop that starts at the last character 
in the string and works its way backwards to the first character 
in the string, printing each letter on a separate line, except backwards.
"""
fruit = 'banana'
leng = len(fruit)
index = leng - 1
stop = 0

while stop < leng:
	index = index -1
	print(fruit[index])
	stop = stop + 1
"""
Exercise 2: Given that fruit is a string, what does fruit[:] mean?

Ans: It's for slicing a string. In this case, the word will not be
sliced since the empty fields for [n:n] means that includes the first
and last character. 
"""

"""
Exercise 3: Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""
def count():
	word = input('Write a word or number: ')
	var = input('Letter or number to be counted: ')
	counted = 0
	for letter in word:
	    if letter == var:
	        counted = counted + 1
	print(counted)

count()

"""
Exercise 4: There is a string method called count that is similar to the function in the previous exercise. 
Read the documentation of this method at:

https://docs.python.org/library/stdtypes.html#string-methods

Write an invocation that counts the number of times the letter a occurs in “banana”.
"""
fruit = 'banana'
count = fruit.count('a')
print(count)

"""
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character 
and then use the float function to convert the extracted string into a floating point number.
"""
str = 'X-DSPAM-Confidence:0.8475'
finding = str.find(':')
snum = str[finding + 1: ]
fnum = float(snum)
print(type(fnum), fnum)

"""
Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods 
You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), 
the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
"""

