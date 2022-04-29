# server.py serves as server in Wordle Unlimited game

import random
from socket32 import create_new_socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Function to create word list from word bank
def create_word_list(number): 
    # Open the word bank
    our_file = open("words.txt", "r") # r means read permissions
    # Read the word bank
    word_data = our_file.read()
    # Replace end splitting the text when newline ('\n') is seen
    word_list = word_data.split("\n")
    # Create new, empty list
    new_list = []
    # Create list where only lowercase words, words without
    # apostrophes, and words of the users inputted desired
    # length are taken into account from the bank
    for i in range(len(word_list)): 
        if word_list[i].islower() and len(word_list[i]) == number and "'" not in word_list[i]:
            # If criteria is matched, append this to word list
            new_list.append(word_list[i])
    # Return the new list
    return(new_list)
    # Close the word bank since not used
    our_file.close()

# Function to check guesses and show color 
def wordle(choice, guess, guesses_past):
    # ANSI colours
    green = "\033[0;32m"
    yellow = "\033[1;33m" 
    reset = "\033[0m"
    red = "\033[1;31m"
    # Create an empty list for the result
    result = []
    # Make word length based off of length of the choice
    word_length = len(choice)
    # Assume word is incorrect initially through coloring it red
    for i in range(word_length):
        result.append(f"{reset}{guess[i]}" + ' ')
    # Create variable for a text input of winning or guessing again 
    result1 = '' 
    if choice == guess: # If player guess is correct or not
        result1 = f'{green}You Win!'
    else:
        result1 = f'{red}Guess Again!'
    # Create a set based on the unique letters in the choice
    uniq_letters = set(choice)
    for i in uniq_letters:
        # Create a set that gives the position for each unique 
        # letter and an empty set if there is no such letter in choice
        choice_set = {pos for pos, char in enumerate(choice) if char == i}
        # Create a set that gives the position for each unique letter 
        # and an empty set if there is no such letter in guess
        guess_set = {pos for pos, char in enumerate(guess) if char == i}
        # Find the elements in the two choice and guess set that are
        # the same (i.e. when the letters of the guess match letter and
        # position of choice)
        intersection = choice_set.intersection(guess_set)
        # Remove the intersection set from both sets to not double count 
        # already accounted for letters
        choice_set = choice_set.difference(intersection)
        guess_set = guess_set.difference(intersection)
        # Make the number of (in wordle) yellow or starred results based
        # on the smallest set. This is to make sure that the number of 
        # yellows are correct
        number_yellow = min(len(choice_set), len(guess_set))
        for j in range(number_yellow):
            # Take the popped element, which is the position of the 
            # yellow letter and use that element for the result
            ele = guess_set.pop()
            result[ele] = f"{yellow}{guess[ele]}" + ' '
        if len(intersection) > 0:
            # If intersection is not an empty set than use that 
            # intersection set to find the position of green letters.
            for i in intersection:
                result[i] = f"{green}{guess[i]}" + ' '
    # Make the list into a string
    result = ''.join(result) 
    # Returns past guesses too and removes previous 'Guess Again!'
    return(guesses_past.replace('Guess Again!', '') + result + '\n' + result1)

def track_letters(choice, guess, past):
    # Preconditions
    track = []
    str = ' '
    
    # For loop to run through the length of the word
    for i in range(len(choice)):
        # Converts the list track into a string for easier iteration
        track_string = str.join(track)
        # Checks if a letter of guess is not in the word, not in 
        # past rounds of guesses, and not in this round of guesses
        if guess[i] not in choice and guess[i] not in past and guess[i] not in track_string:
            # Adds letter to the list
            track.append(guess[i])
    # Convert the string 'past' to a list
    list = past.split()
    # Join tw lists
    final = list + track
    # Sorts the letter list alphabetically
    final.sort()
    
    # Convert list to a string
    string = str.join(final)
    return(string)

def main():
    
    with create_new_socket() as s:
        # Creates a connection with the client
        s.bind(HOST, PORT)
        s.listen()
        print("WORDLE UNlIMITED server started. Listening on", (HOST, PORT))

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            while True:
                letters = conn.recv()
                w_list = create_word_list(int(letters))
                # Make a random choice
                choice = random.choice(w_list)
                print(f'Wordle Word: {choice}')
            
                # Create response to indicate how long the chosen word is
                # Empty initial response
                response = '' 
                for i in range(len(choice)):
                    # Put underscore to indicate the length, 
                    # make new 'response'
                    response = response + '_ '
                word_length = len(choice)
                break

            
            # Send the message to client in how long the word is
            message = choice + ';' + f'Word: {response}  (the word has a length of {word_length})'
            conn.sendall(message)

            turn = 0
            past = ''
            guesses_past = ''
            reset = "\033[0m"

            while True:
                guess = conn.recv() # Receive the player's guess
                # Checks if the length of the guess matches the 
                # computer choice and also if the word is a valid 
                # word based on our word list
                if (len(guess) == len(choice) and guess in w_list):
                    # Counts the turn
                    turn = turn + 1
                    # Puts past letters not in word into a string
                    past = track_letters(choice, guess, past)
                    # Edits from past guesses
                    guesses_past = wordle(choice, guess, guesses_past)
                    message = guesses_past + '\n' + f'{reset}Letters Used: ' + past + '\n' + f'Number of Guesses: {turn}'
                    conn.sendall(message)
                else: # Doesn't work if it is not valid from above
                    conn.sendall('Guesses must be a valid word and have the same number of letters as the wordle word. Try again...')
                
                if not guess: # If something went wrong, then we break
                    break

            print('Disconnected')

if __name__ == '__main__':
   main()