# CS-32-FP (Wordle Unlimited)

CS32 Final Project for Group 1 (Brian Kim, Allison Park, Dylan Park)

## Replit Link for the Final Project

https://replit.com/join/rjdmxiaftl-allisonskypark

## Our Plan

Dylan, Brian, and Allison intend to make an expanded version of Wordle called Wordle Unlimited. Wordle is currently a popular game, in which users have 6 attempts to guess the 5-letter word of the day. With each guess, Wordle checks each letter of the user’s answer and tells the user whether or not the letters of their guess are in the actual word and if the correct letter is in the right location. Our version will have a word of variable length (5 to 10 letters), but otherwise function similarly to Wordle. We also decided to call it Wordle Unlimited because users have an unlimited amount of guesses. Some tools from class that we will be utilizing are accessing a set of words from a txt file, using server and client relations, and utilizing ANSI values for color.

## Online Resources

Word list from https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=markup

## First Steps

We started by downloading and uploading a word list and then we created a function to revise the word list to better fit our functions. In this case, the criteria we use are that words have to be lowercase, they must be greater than 3 letters, and doesn't have any punctuations (apostrophe, comma, and period). We also worked on the guess checker as well, allowing the server to receive a guess and check the player guess with the actual word, giving back different feedback depending on the letters and their position.

## How the Code Works

It takes the user prompt to decide the length of the word and generates a random word with that length on the server. It will then provide a blank space for the amount of letters in the word and prompts the user to input a valid word (i.e. same number of letters and a word in english). This will then give the user an output that contains green letters for letters in the guess that are in the correct space and yellow for letters that are in the wrong space. Letters in the guess that are not in the actual word will show up as the standard console color (in replit, white). This input cycle of a valid word and the subsequent response continues until the user guesses the correct word. The output will also give the number of guesses and the past results for each input as well as an alphabetical list of incorrect letters already used in the guess.


## Description of File

`socket32.py`, `check32.py`: Scripts used in Problem Set 2 for CS32 to put a simpler interface on the `socket` library and used to create a client-server relationship in the game Wordle Unlimited.

`server.py`: Script that serves as the server for the Wordle Unlimited game that runs all three functions explained below, generates a random word, and ends the game.

`client.py`: Script that serves as the client for the Wordle Unlimited game so that the player can input word guesses and specify the length of the word in the game they want to play. Disconnects when game is over.

`words.txt`: txt file containing the word list imported from website linked in the online resources section

`output.txt`: txt file created from `test2.py` to essentially test the `create_word_list(number)` function

`test1.py`: Script that is used exclusively as a tester function to test `wordle(choice, guess, guesses_past)`

`test2.py`: Script that is used exclusively as a tester function to test `create_word_list(number)`and outputs result into `output.txt`

`test3.py`: Script that is used exclusively as a tester function to test the functionality of `track_letters(choice, guess, past)`

## Functions in `server.py`

`create_word_list(number)`: Opens a txt file of a wordbank (`words.txt`) from the URL above and returns a simplified word list that only contains lowercase letters, words without apostrophes, and words with a length as specified by the user (`number`). 

`wordle(choice, guess, guesses_past)`: Takes in the actual word (`choice`), the guess (`guess`), and the past results (`guesses_past`). Checks the user's input, default text color (white in Replit) shows incorrect letter guesses, green color shows letter guess in the right place, and yellow color shows correct letter guesses but in incorrect place. Just like the game Wordle, if one letter is used in multiple places, only one letter in one place will feature some color. If that place is the correct guess, then the function will prioritize the letter in that correct location to show the green color. Otherwise, it will show a yellow in one of the places (meaning the letter was placed incorrectly in both locations).

`track_letters(choice, guess, past)`: Tracks the letters used by the client that are not actually in the randomly-generated word the computer chose (`choice`). Client would guess a word (`guess`) and letters in `guess` that are not actually in choice would be added to a list that includes past incorrect letters(`past`) as well. The function ultimately converts the list into a string that will be outputted and printed to show the client wrong letters already used. Will not show correct letters.

## Limitations (Potential Improvements): 

The clarity of our code could have been improved if we had started with classes in order to track the game-state of our code. This would have allowed us to track the past guesses and their results in another way and would have been clearer code to the reader.

We also acknowledge that the word list does not contain every single word that exists, but we found this word list from an online resource and it still initially has 25,488 words inputted in, which for the purposes of this project should be comprehensive enough.



