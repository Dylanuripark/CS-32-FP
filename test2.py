# test2.py essentially runs a version of create_word_list() function from server.py and places the output list in output.txt


import json

# Change the int assigned to number according to your desired number of letters of your word
number = 5

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

with open("output.txt", "w") as f: # w means write permissions
    f.write(json.dumps(new_list))
# Close the word bank since not used
our_file.close()