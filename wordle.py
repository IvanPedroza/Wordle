# Import necessary modules
import random
import os
from sys import argv

os.system("")   # Clear the terminal

# Define text formatting codes
G = '\x1b[0;30;42m'  # Green text
Y = '\x1b[0;30;43m'  # Yellow text
N = '\x1b[0m'        # Normal text/no highlighting

# Constants for the game
ALLOWED_GUESSES = 6
WORD_LENGTH = 5

# Function to color code the letters of the word guessed based on placement of the letters
def format_guess(guess, word):
    """
    format_guess(): formats a colored string for printing and evaluates the guess
    Parameters: guess (string), word (string)
    Returns a formatted guess string and a boolean indicating if the guess is correct
    """
    formatted_guess = []
    is_correct_word = False

    # Iterate through letters of a guess, access their placement and correctness, and color the letters
    for i in range(len(guess)):
        if guess[i] == word[i]:
            formatted_guess.append((G + guess[i]))  # Correct letter in the correct position (Green)
        elif guess[i] in word:
            formatted_guess.append((Y + guess[i]))  # Correct letter in the wrong position (Yellow)
        else:
            formatted_guess.append((N + guess[i]))  # Incorrect letter (Normal)
    formatted_guess.append(N)  # Reset text formatting
    guess_string = "".join(formatted_guess)

    if guess == word:
        is_correct_word = True

    return guess_string, is_correct_word

# Function to select a word from word bank for the guessing
def get_valid_words():
    """
    get_valid_words(): Reads valid words from a nltk English word bank and selects a random word
    Returns a valid word (string)
    """
    scrabble_words = open("Scrabble Words.txt")
    #creates list of specified len from text file
    words_list = [word for line in scrabble_words for word in line.split() if len(word) == WORD_LENGTH]
    word = random.choice(words_list).upper()
    return word

# Main function -- contains driver code with game specifications
def main(given_parameter=None):
    """
    Main(): Starts the Wordle puzzle game and prompts the user for guesses

    Parameters:
    - given_parameter (str, optional): An optional parameter that allows the user to provide a target word
      as a command-line argument. If not provided, a random valid word is selected.
    """
    print(f"Welcome to {Y}PY{G}WOR{Y}D{G}LE{N}!")

    if given_parameter:
        word = given_parameter.upper()
    else:
        word = get_valid_words()

    failed_guesses = []  # Store formatted guesses
    user_guess = ""

    # Promts user to guess until word is guessed correctly or max attempts are reached
    while user_guess != word and len(failed_guesses) != ALLOWED_GUESSES:
        user_guess = input(f"Guess the {WORD_LENGTH} letter word: ").upper()
        if len(user_guess) > WORD_LENGTH:
            print("Invalid word length! Try Again!")
            next
        else:
            formatted_guess, is_correct = format_guess(user_guess, word)
            failed_guesses.append(formatted_guess)
            print(*failed_guesses, sep="\n")  # Print all previous guesses

            if is_correct is True:
                print(f"Congrats! You figured it out in {len(failed_guesses)} tries!")
                exit()
    print(f"Sorry, the word was {word}. Try another puzzle!")

if __name__ == "__main__":
    if len(argv) == 2:
        main(argv[1])  # If a word is provided as a command-line argument, use it as the target word
    else:
        main()  # Otherwise, generate a random target word
