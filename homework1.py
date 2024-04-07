# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE: Jenny Jiani Zhong 
# YOUR GITHUB USER NAME HERE: datapolicypython

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work. 

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

my_dict = {'a':5, 'b': 10, 'c':15, 'd':20}

for key, val in my_dict.items():
    print('The value at position', key, 'is', val)


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

#I used this website for reference for removing punctuation: https://blog.enterprisedna.co/python-remove-punctuation-from-string/#:~:text=To%20remove%20punctuation%20from%20a,new%20string%20excluding%20punctuation%20marks.
#I also used this website for removing white spaces in the translate function: https://www.scaler.com/topics/remove-whitespace-from-string-python/

import string

radar = "radar"
phrase = "A man, a plan, a canal, Panama!"
microsoft = "microsoft" 
nahpal = "This isn't a palindrome"

def thisisapalindrome(x):
    x = x.lower()
    translation = str.maketrans('', '', string.punctuation + " ")
    x = x.translate(translation)
    if (x == x[::-1]):
            return "This string is a palindrome!"
    else: 
            return "This string is not a palindrome :("

thisisapalindrome(radar)
thisisapalindrome(phrase)
thisisapalindrome(microsoft)
thisisapalindrome(nahpal)

# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

#I searched up: "how to start a loop that allows user input repeatedly python?" 
#used this youtube video: https://www.youtube.com/watch?v=c4egW80OBfA&ab_channel=CalebCurry

while True:
    choice = input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print('Yes, you may have this vegetable. That will be $1 million.')
        break  
    else: 
        print('Sorry we do not have this vegetable, please pick another!')

# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

import string

sentenceaboutabear = ['An', 'adventurous', 'bear', 'curious', 'about', 'discovering', 'every', 'forest', 'gallantly', 'hopped']

processed_sentence = []

for string in sentenceaboutabear:
    lowerlower = string.lower()
    if not lowerlower.startswith(('a', 'b')):
        processed_sentence.append(lowerlower)

print(processed_sentence)


# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

dictcomp = {short_names[i]: long_names[i] for i in range(len(short_names))}

print(dictcomp)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def twoargu(x, y):
    summed = x + y
    if summed > 10:
        return "big"
    elif summed == 10: 
        return "just right"
    else:
        return "small"
    
end_list = [twoargu(x, y) for (x, y) in start_list]
print(end_list)

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()
print(x)

#New code

def newfunc(newnum):
    b = 40 
    answerup = b + newnum
    return answerup 
newfunc(10)


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True. If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:

import string 

import random

randominteger = string.digits
randomsymbols = "!@#$%^&*"
randomlettersL = string.ascii_lowercase
randomlettersU = string.ascii_uppercase

def password(length):
    character_list = randominteger + randomlettersL + randomsymbols + randomlettersU 
    password = []
    if length < 8: 
        return print("Warning: Password length must be betewen 8 and 16.")
    elif length > 16:
        return print("Warning: Password length must be between 8 and 16.")
    else: 
        for i in range(length):
            random_char = random.choice(character_list)
            password.append(random_char)
        return"".join(password)

password(14)
password(10)

  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

#i learned from here: https://www.w3schools.com/python/python_classes.asp

import random

class MovieDatabase:
    def __init__(self, name_of_creator):
        self.name_of_creator = name_of_creator
        self.movieinfo = []
        
    def add_movie(self, movie_name, genre, rating):
        movie_details = {
            'movie name': movie_name,
            'genre': genre,
            'rating': rating
        }
        self.movieinfo.append(movie_details)
        
    def what_to_watch(self):
        if not self.movieinfo: 
            print("Add movies to database")
        else: 
            movie = random.choice(self.movieinfo) 
            print(f"You can watch this movie '{movie['movie name']}' ({movie['genre']}, rated {movie['rating']}) courtesy of {self.name_of_creator}.")

mdb = MovieDatabase("Bob")

mdb.add_movie("The Godfather", "thriller", "4")
mdb.add_movie("The Shawshank Redemption", "crime", "5")
mdb.add_movie("Shutter Island", "thriller", "4")
mdb.add_movie("Schindler's List", "history", "5")

# Now calling the what_to_watch method
mdb.what_to_watch()


