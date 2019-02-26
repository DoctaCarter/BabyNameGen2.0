# Input desired last name, gender, first initial. Code will pull names from txt file and combine customize name.

import re

last_name = input("Choose your baby's last name: ")
gender = input("Will it be a boy or girl? ")
letter = input("What would you want their first initial to be? ")
pattern = re.compile(letter.capitalize(), 0)
results = 0

if gender.lower() == "boy":
    with open('boynames.txt', 'rt') as in_file:  # Open file boynames.txt for reading of text data.
        for line in in_file:  # Store each line in a string variable "line"
            if pattern.search(line):
                results += 1
                print(last_name.capitalize()+", "+line)  # Print last name and first name

if gender.lower() == "girl":
    with open('girlnames.txt', 'rt') as in_file:  # Open file boynames.txt for reading of text data.
        for line in in_file:  # Store each line in a string variable "name"
            if pattern.search(line):
                results += 1
                print(last_name.capitalize()+", "+line)  # Print last name and first name

print("Total baby name results: ", results)
