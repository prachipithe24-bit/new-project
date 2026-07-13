# 🔐 Password Generator & Strength Checker

A command-line Python tool that generates secure random passwords and checks the strength of any password you give it.

## Features
- 🎲 Generate random passwords with customizable length
- 🔠 Choose whether to include uppercase letters, numbers, and symbols
- 💪 Check the strength (Weak / Moderate / Strong) of any password
- 🖥️ Simple, interactive command-line menu

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. Run the app:
   ```bash
   python password_generator.py
   ```

## Requirements
- Python 3.6 or higher (no external libraries needed — uses only built-in `random` and `string` modules)

## Example

```
==== PASSWORD GENERATOR ====

1. Generate a new password
2. Check strength of my own password
3. Exit
Choose an option (1-3): 1
Password length (default 12): 16
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password: xT8@kLp!qR2#zM9w
Strength: Strong
```

## How Strength is Scored
Points are awarded for:
- Length ≥ 8 characters
- Length ≥ 12 characters
- Contains lowercase letters
- Contains uppercase letters
- Contains numbers
- Contains symbols

Total score determines the rating: Weak, Moderate, or Strong.

## Future Improvements
- Add a GUI using Tkinter
- Check passwords against common leaked password lists
- Add option to exclude ambiguous characters (like `l`, `1`, `O`, `0`)

## Author
Prachi
