# Wordle Puzzle Game 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)](https://github.com/IvanPedroza/Wordle)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/IvanPedroza/Wordle)


A text-based Python implementation of the popular Wordle puzzle game. Players attempt to guess a hidden five-letter word within six tries. After each guess, the game provides immediate visual feedback:

- **Green**: Correct letter in the correct position.
- **Yellow**: Correct letter in the wrong position.
- **Default**: Letter not in the word.

## Quick Start

Follow these instructions to set up and play the game on your local machine.

### Prerequisites

- **Python** installed on your system ([Download Python](https://www.python.org/downloads/)).

> **Note for macOS users:** Python is no longer pre-installed on macOS Catalina and later versions. Please install Python manually.

### Installation & Running the Game

1. Clone this repository:

```bash
git clone https://github.com/IvanPedroza/Wordle.git
cd Wordle
```

2. Run the game:

```bash
python wordle.py
```

Optionally, specify your own target word (must be 5 letters):

```bash
python wordle.py MYWORD
```
Replace `MYWORD` with your custom word.

## Gameplay

- Start the game and enter your guesses when prompted.
- Receive color-coded feedback for each letter:
  - **Green**: Letter is correctly placed.
  - **Yellow**: Letter exists but is incorrectly placed.
  - **Default**: Letter is not part of the word.
- You have **6 attempts** to guess correctly.
- After your attempts:
  - Success: A congratulatory message shows the number of attempts.
  - Failure: The correct word is revealed.

## Customizing the Word Bank

The default word bank uses a local text file (`Scrabble Words.txt`). For expanded or dynamic word banks, consider integrating:

- **APIs**: [Wordnik](https://www.wordnik.com/)
- **Python Libraries**: [NLTK](https://www.nltk.org/) or [spaCy](https://spacy.io/)

This can provide more variety and enhance gameplay.

## License

This project is distributed under the [MIT License](https://github.com/IvanPedroza/Wordle/blob/main/LICENSE).

## Acknowledgments

Inspired by the original Wordle puzzle game by The New York Times.

Enjoy playing!

