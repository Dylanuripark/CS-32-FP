# test3.py is a tester code for the function track_letters(choice, guess, past) in server.py

# Edit to the words you want when testing
choice = 'often' 
guess = 'apple'

past = ''

# Preconditions
track = []
track_string = ''
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
print(string)
