# Wordle Puzzle Game

A Python program that implements a text-based version of the Wordle puzzle game. In Wordle, the player must guess a target word within a limited number of attempts. The program provides feedback on the correctness of each guess, including coloring the letters to indicate whether they are in the correct position (green), in the word but in the wrong position (yellow), or not in the word (normal).

## Getting Started

These instructions will help you run the Wordle puzzle game on your local machine.

### Prerequisites

You need to have Python installed on your machine to run this program. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

### Installation

1. Clone or download the code from this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the code.

3. Run the game by using the following command: `python wordle.py`

   You can also provide a custom word as a command-line argument: `python wordle.py MYWORD`
   
   Replace `MYWORD` with your custom 5-letter word.

### Using Other Libraries for Word Bank

By default, this program uses a text file as a word bank to select a random word for the game. However, you can explore using other libraries and APIs to pull words dynamically. For example, you can integrate APIs like Wordnik or use Python libraries such as NLTK or spaCy to fetch words from various sources. This allows you to have a more extensive and dynamic word bank for the game.

## How to Play

1. When you start the game, you will be greeted with a welcome message.

2. You have to guess a 5-letter word.

3. Enter your guess, and the program will provide feedback on the correctness of your guess.

4. If a letter is in the correct position, it will be displayed in green.

5. If a letter is in the word but in the wrong position, it will be displayed in yellow.

6. If a letter is not in the word, it will be displayed in the default text color (usually white).

7. You have a maximum of 6 attempts to guess the word correctly.

8. If you guess the word correctly, the program will congratulate you and display the number of attempts it took.

9. If you run out of attempts, the program will reveal the correct word.

## Contributing

If you'd like to contribute to this project, feel free to open issues, submit pull requests, or make suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the Wordle puzzle game.

Happy gaming!


