"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""
word_dict = {}  

file =open("words.txt")
for line in file:
    words = line.strip().split()  
    for word in words:
        word_dict[word] = None 


user_input = input("Enter a word: ")
if user_input in word_dict:
    print("The word exists in the dictionary.")
else:
    print("The word does not exist in the dictionary.")

"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).
"""
file = open('mbox-short.txt')
day_count = {}  

for line in file:
    if line.startswith("From"):
        words = line.split()
        if len(words) >= 3:
            day = words[2]
            day_count[day] = day_count.get(day, 0) + 1

print(day_count)

"""
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count 
how many messages have come from each email address, and print the dictionary.
"""
file = open('mbox-short.txt')
email_count = {} 

for line in file:
    if line.startswith("From"):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            email_count[email] = email_count.get(email, 0) + 1

print(email_count)

"""
Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary 
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
and print how many messages the person has.
"""
fname = input("Enter file name: ")
fh = open(fname)
dc = {}

#get the emails from the text
for emails in fh:
    #find the emails
    if emails.startswith('From '):
        mail = emails.rstrip()
        mail = mail.split()
        l = mail[1]
        l = l.split()
    #l = list of emails

        #add to the dictionary
        for k in l:
            dc[k] = dc.get(k, 0) + 1

#find the bigest one and his key
bc = None
bw = None
for word,count in dc.items():
    if bc is None or count > bc:
        bc = count
        bw = word

print(bw, bc)

"""
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the whole email address). 
At the end of the program, print out the contents of your dictionary.
"""
file = open('mbox-short.txt')

domain_count = {}  
for line in file:
    if line.startswith("From"):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            domain = email.split("@")[1]  # Extract the domain name
            domain_count[domain] = domain_count.get(domain, 0) + 1
print(domain_count)

