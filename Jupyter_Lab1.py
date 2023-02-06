#!/usr/bin/env python
# coding: utf-8

# In[1]:


#See the list below.
#  Please write a program that will tell you what the longest word is in the list.
#  Package your program inside of a function.

def longest_wrd():
    list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
    length_list = []
    longest_word_list = []
    for x in list:
        length_list.append(len(x))
    longest_word_length = max(length_list)
    for x in list:
        if longest_word_length == len(x):
            longest_word_list.append(x)
    print(f"The word(s) that is/are the longest: {longest_word_list}")
longest_wrd()


# In[38]:


# Now that you have built the program above,
#in a new cell, edit your program: import a .txt file of a list of words
#and have your program randomly choose 7 words from the file to add to a list,
#and then have the program determine the longest word as you did above.
import random

f = open("txtdoc.txt")
read = f.read()
read_list = read.split(",")

global seven_list
seven_list = random.sample(read_list, 7)

print(seven_list)


def longest_wrd():
    global seven_list
    #list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
    length_list = []
    longest_word_list = []
    for x in seven_list:
        length_list.append(len(x))
    longest_word_length = max(length_list)
    for x in seven_list:
        if longest_word_length == len(x):
            longest_word_list.append(x)
    print(f"The word(s) that is/are the longest: {longest_word_list}")
longest_wrd()


# In[51]:


# Pretend that you're going to be leading a review session on dictionaries.
# Build a program that uses dictionaries and incorporates at least 4 built-in methods. 
import time

practice_dict = {"John": "Sophomore",
                "Alex": "Sophomore",
                "Freud": "Sophomore"}

class Dictionary:
    def __init__(self, dict_):
        self.dict = dict_
        
    def demonstrate_copy(self):
        print("Another built-in method of dictionaries is .copy()")
        time.sleep(1)
        dict2 = self.dict.copy()
        print(f"The original dict: {self.dict}.")
        time.sleep(1)
        print(f"The copied dict: {dict2}.")
        
    def demonstrate_clear(self):
        print("One built in-method for a dictionary is the .clear method.")
        time.sleep(1)
        print("This method clears the dictionary of all values.")
        print(f"Original dictionary: {self.dict}")
        self.dict.clear()
        print(f"Cleared dictionary: {self.dict}")
        
    def demonstrate_update(self):
        print(".update() is another useful built-in method for dictionaries!")
        time.sleep(1)
        print("It is used to add items to the dictionary")
        time.sleep(1)
        print(f"Original dictionary: {self.dict}")
        time.sleep(1)
        self.dict.update({"Ed": "Junior"})
        print(f"Updated dictionary: {self.dict}")
    def demonstrate_pop(self):
        print(".pop can remove a specified item")
        time.sleep(1)
        self.dict.pop("John")
        print(f"After using .pop: {self.dict}")
        time.sleep(1)
        print(".popitem can be used to remove the last item on the dictionary")
        self.dict.popitem()
        print(self.dict)
        
x1 = Dictionary(practice_dict)

x1.demonstrate_copy()

x1.demonstrate_update()

x1.demonstrate_pop()

x1.demonstrate_clear()


# In[52]:


# Using OOP, I want you to build one of the following things.
# As part of the excerise, please write out your brainstorming process in a comment or markdown cell:
#A system to manage a student's school record
#(would need a way to gather/store personal information, record grades, record GPA, etc.)


# In[ ]:


# Brainstorming: I'm choosing to make a class to create manage a students school record
# In order to do this Im going to create a Student class and ask for some information from the user. 
# Then I'm going to make a method that return that info and then 2 more methods 1 to record grades
# and another one to record GPA.


# In[172]:


class Student:
    def __init__(self, name, rank, age):
        self.name = name
        self.rank = rank
        self.age = age
        
    def return_info(self):
        print(f"Name: {self.name}")
        time.sleep(0.5)
        print(f"Rank: {self.rank}")
        time.sleep(0.5)
        print(f"Age: {self.age}")
        time.sleep(0.5)
        
    def record_grades(self):
        question = int(input("How many grades would you like to put in?"))
        while question > 0:
            dict1 = {}
            lock = input("What class is this grade for?")
            key = int(input("What grade was gotten?"))
            dict1.update({lock: key})
            question -= 1
        print(dict1)
            
    def record_gpa(self):
        gpa_question = int(input("What is your GPA?"))
        print(f"GPA: {gpa_question}")

            
x1 = Student("Edward", "Sophomore", 20)

x1.return_info()
x1.record_grades()
x1.record_gpa()


# In[180]:


#Finalize your Hangman program and submit it. 
#Include any necessary comments and explain what you had "refreshed" by building it in class.
#If appropriate, use functions or OOP to package the pieces of your code.



import random
import time

words = ["twelve", "four", "fire", "road", "elf", "pyramid", "pirate", "code",
        "building", "star"]


global chances
chances = 6

def word_pick():
    global selected_word
    selected_word = random.choice(words)
word_pick()

global game_ui
game_ui = []

def game_ui_creation():
    global game_ui
    char_amt = len(selected_word)
    while char_amt > 0:
        game_ui.append("_")
        char_amt -= 1
game_ui_creation()

def intro():
    print("Welcome to Hangman!")
    time.sleep(1)
    print("Let's Start!")
    time.sleep(1)
    print(f"The word you have to guess has {len(selected_word)} characters")
    time.sleep(1)
    print(f"Here is the game board: {game_ui}")
intro()

global correct_guess
correct_guess = []

global guessed_chars
guessed_chars = []

global right_guess
right_guess = False

global broken
broken = False

def guess_a_letter():
    global right_guess
    global chances
    global broken
    while chances > 0: 
        broken = False
        right_guess = False
        count = -1
        guess = input("What letter would you like to guess?")
        if guess in guessed_chars:
            print("You have already guessed that letter! Try Again!")
            broken = True
            break
        guessed_chars.append(guess)
        for x in selected_word:
            count += 1
            if x == guess:
                right_guess = True
                time.sleep(1)
                print("You have guessed a letter correctly!")
                correct_guess.append(guess)
                time.sleep(1)
                game_ui.pop(count)
                game_ui.insert(count, guess)
                print(f"Here is your current progress: {game_ui}")

        if right_guess == False:
            chances -= 1
            time.sleep(1)
            print(f"You have guessed incorrectly! You have {chances} chances left!")
            
        elif len(correct_guess) == len(selected_word):
            print("You have guessed all the letters and won!")
            broken = False
            time.sleep(1)
            break
guess_a_letter()

if broken == True:
    guess_a_letter()
else:
    print("Thanks for playing!")
    




# In[ ]:





# In[ ]:




