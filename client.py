# WordleUnlimited -- client
from server import create_word_list
from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def main():
    print('## Welcome to Wordle Unlimited! ##')
                
    with create_new_socket() as s:
        s.connect(HOST, PORT)

        # Ask for what user wants in number of letters in words
        while True:
            try:
                # Ask for input
                letters = int(input('Number of letters you want word to be (from 5 to 10): '))
                # Conditionalize for it to be in between 5 and 10
                if letters < 5 or letters > 10:
                    print("Input must be an integer from 5 to 10")
                    # Returns back to the beginning of the loop
                    # if this part of the code runs
                    continue
                # Send the number of letters for word list to be
                # generated
                s.sendall(str(letters))
                break
            # Runs if input is not an integer
            except ValueError:
                    print("Input must be an integer from 5 to 10")
            
        # Receive from client message of how long the word is 
        # and blanks
        initial_message = s.recv()
        message_list = initial_message.split(';')
        # Print out the long message with length
        print(message_list[1])
        word = message_list[0]
        
        # Grab a valid guess from the player
        while True:
            guess = str(input('Please guess a word: '))
            # Sends player's guess back to the computer
            s.sendall(guess.lower())
            response = s.recv()
            print(response)
            # Check if the guess is the actual word and 
            # end the game
            if word == guess:
                break

if __name__ == '__main__': 
    main()