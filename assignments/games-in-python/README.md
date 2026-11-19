# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman word-guessing game in Python using strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the game data and initialize the variables needed to track the player's progress.

#### Requirements
Completed program should:

- Store a predefined list of words.
- Randomly select one word from the list.
- Track the letters the player has guessed.
- Track the number of incorrect guesses remaining.
- Display the hidden word using underscores for unguessed letters.

### 🛠️ Implement the Guessing Loop

#### Description
Add the main gameplay loop that accepts letter guesses and updates the game state.

#### Requirements
Completed program should:

- Prompt the player to enter a letter.
- Accept and process one letter at a time.
- Update the display to reveal correctly guessed letters.
- Record incorrect guesses and reduce the attempts remaining.
- Continue until the word is fully guessed or the attempts are exhausted.

### 🛠️ Complete the Game

#### Description
Finish the game flow and provide clear feedback to the player.

#### Requirements
Completed program should:

- Display a win message when the player guesses the full word.
- Display a loss message and reveal the hidden word when the player runs out of attempts.
- Prevent repeated guesses from reducing the remaining attempts.
- Print clear status messages throughout the game.
