# test1.py is the tester code for the main wordle() function in server.py
green = "\033[0;32m"
yellow = "\033[0;33m"
reset = "\033[0m"
red = "\033[1;31m"

# Edit to the words you want when testing
choice = 'proverb' 
guess = 'picture'
guesses_past = ''

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
        result[ele] = f"{yellow}{guess[ele]}"
    if len(intersection) > 0:
        # If intersection is not an empty set than use that 
        # intersection set to find the position of green letters.
        for i in intersection:
            result[i] = f"{green}{guess[i]}" + ' '
# Make the list into a string
result = ''.join(result) 
# Returns past guesses too
print(guesses_past.replace('Guess Again!', '') + result + '\n' + result1)