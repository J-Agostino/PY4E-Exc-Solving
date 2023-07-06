"""
Exercise 1: Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None. Then write a function 
called middle that takes a list and returns a new list that contains all but the first and last elements.
"""
def chop(lst):
    if len(lst) >= 2:
        del lst[0]  # Remove the first element
        del lst[-1]  # Remove the last element
    else:
        lst.clear()  # Clear the list if it has less than 2 elements
    return None

def middle(lst):
    if len(lst) >= 3:
        return lst[1:-1]  # Return a new list containing all but the first and last elements
    else:
        return []  # Return an empty list if the input list has less than 3 elements

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

chop(my_list)
print("Modified list (chop):", my_list)

my_list = [1, 2, 3, 4, 5]
result = middle(my_list)
print("New list (middle):", result)

"""
Exercise 2: Figure out which line of the above program is still not properly guarded. 
See if you can construct a text file which causes the program to fail and then modify the 
program so that the line is properly guarded and test it to make sure it handles your new text file.

new-text.txt
From something to something
From
From something

To form something
From test testing
From hello world
"""
fhand = open('new-text.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    #print(len(words))
    if len(words) >= 3: #This line will prevent the program to stop when there's only the word 'From' in a line
        print(words[2])
    else: continue

"""
Exercise 3: Rewrite the guardian code in the above example without two if statements. 
Instead, use a compound logical expression using the or logical operator with a single if statement.
"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From' and len(words) >= 3:
        print(words[2])

"""
Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you determine that? 
How would you produce the list of all the words that Shakespeare used? Would you download all his work, 
read it and track all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, 
that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, 
which will contain the final result. Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function. For each word, 
check to see if the word is already in the list of unique words. If the word is not in the list of unique words, 
add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)

"""
Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of emails. 
This was used by early email servers and desktop apps. Without getting into too many details, 
MBOX is a text file, which stores emails consecutively. Emails are separated by a special line 
which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) 
describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, 
that lists the email of the senders in the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, 
you will split the line into words using the split function. We are interested in who sent the message, 
which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line, then you will also 
count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:
"""
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for emails in fh:
    if emails.startswith('From '):
        mail = emails.rstrip()
        mail = mail.split()
        count = count + 1
        print(mail[1])
print("There were", count, "lines in the file with From as the first word")

"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the 
maximum and minimum of the numbers at the end when the user enters “done”. 
Write the program to store the numbers the user enters in a list and use the max() and min() 
functions to compute the maximum and minimum numbers after the loop completes.
"""
numbers = []  # Empty list to store the numbers

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input == 'done':
        break
    
    try:
        number = float(user_input)  # Convert user input to a float
        numbers.append(number)  # Add the number to the list
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if numbers:
    print("Maximum number:", max(numbers))
    print("Minimum number:", min(numbers))
else:
    print("No numbers entered.")

