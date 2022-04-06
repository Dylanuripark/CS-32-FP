# CS-32-FP
Our CS32 Final Project (Dylan Park, Brian Kim, Allison Park)

## Our Plan
Dylan, Brian, and Allison intend to make an expanded version of Wordle called Wordle Unlimited. Wordle is currently a popular game, in which users have 6 attempts to guess the 5-letter word of the day. With each guess, Wordle checks each letter of the user’s answer and tells the user whether or not the letters of their guess are in the actual word and if the correct letter is in the right location. Our version will have a word of variable length, but otherwise function similarly to Wordle. Some tools from class that we will be utilizing are accessing a dictionary of set words, using server and client relations, and utilizing RGB values. 

## Online Resources
Word list from https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=markup

## First Steps
We started by downloading and uploading a word list and then we created a function to revise the word list to better fit our functions. In this case, the criteria we use are that words have to be lowercase, they must be greater than 3 letters, and doesn't have any punctuations (apostrophe, comma, and period).

## Description of file
`socket32.py`, `check32.py`: Scripts used in Problem Set 2 for CS32 to put a simpler interface on the `socket` library and used to create a client-server relationship in the game Wordle Unlimited.

`main.py`: Script that serves as the server for the Wordle Unlimited game to generate a random word

## Functions

### `main.py`
create_word_list(): Opens a txt file of a wordbank from the URL above and returns a simplified word list based on criteria defined in First Steps.

