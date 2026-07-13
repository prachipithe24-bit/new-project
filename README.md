# 🎯 Number Guessing Game

A simple command-line game where you try to guess a random number between 1 and 100 within 7 attempts.

## Features
- 🎲 Random number generation between 1 and 100
- 💡 Hints ("Too high" / "Too low") after each guess
- 🔢 Tracks number of attempts used
- 🔁 Option to play again after each round

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game
   ```

2. Run the game:
   ```bash
   python guessing_game.py
   ```

## Requirements
- Python 3.6 or higher (uses only the built-in `random` module)

## Example

```
==== NUMBER GUESSING GAME ====

I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.

Enter your guess: 50
Too high!

Attempts left: 6

Enter your guess: 25
Too low!

Attempts left: 5

Enter your guess: 37
🎉 Correct! You guessed it in 3 attempts.

Play again? (y/n): n
Thanks for playing! Goodbye!
```

## Future Improvements
- Add difficulty levels (change range or attempts)
- Track high scores across sessions
- Add a GUI version using Tkinter

## Author
Prachi
