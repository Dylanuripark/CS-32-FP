# CS-32-FP
CS32 Final Project for Group 1 (Brian Kim, Allison Park, Dylan Park)

# Replit link for the game
https://replit.com/join/rjdmxiaftl-allisonskypark

## Our Plan
Dylan, Brian, and Allison intend to make an expanded version of Wordle called Wordle Unlimited. Wordle is currently a popular game, in which users have 6 attempts to guess the 5-letter word of the day. With each guess, Wordle checks each letter of the user’s answer and tells the user whether or not the letters of their guess are in the actual word and if the correct letter is in the right location. Our version will have a word of variable length, but otherwise function similarly to Wordle. Some tools from class that we will be utilizing are accessing a dictionary of set words, using server and client relations, and utilizing RGB values. 

## Online Resources
Word list from https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=markup

## First Steps
We started by downloading and uploading a word list and then we created a function to revise the word list to better fit our functions. In this case, the criteria we use are that words have to be lowercase, they must be greater than 3 letters, and doesn't have any punctuations (apostrophe, comma, and period). We also worked on the guess checker as well, allowing the server to receive a guess and check the player guess with the actual word, giving back different feedback depending on the letters and their position.

## Description of file
`socket32.py`, `check32.py`: Scripts used in Problem Set 2 for CS32 to put a simpler interface on the `socket` library and used to create a client-server relationship in the game Wordle Unlimited.

`main.py`: Script that serves as the server for the Wordle Unlimited game to generate a random word

`client.py`: Script that serves as the client for the Wordle Unlimited game so that the player can input word guesses

`words.txt`: txt file containing the word list imported from website linked in the online resources section

`file1.txt`: txt file containing only a few words to use as a tester

`dylan.py`: Script that is used exclusively as a tester function

## Functions

### `server.py`
`create_word_list()`: Opens a txt file of a wordbank from the URL above and returns a simplified word list based on criteria defined in First Steps.

`wordle()`: Checks the user's input, default text color (white in Replit) shows incorrect letter guesses, green color shows letter guess in the right place, and yellow color shows correct letter guesses but in incorrect place. Just like the game Wordle, if one letter is used in multiple places, only one letter in one place will feature some color. If that place is the correct guess, then the function will pioritize the letter in that correct location to show the green color. Otherwise, it will show a yellow in one of the places (meaning the letter was placed incorrectly in both locations). 



