# HARDWORD CO

HARDWORD CO is a simple and interactive word-hunting game where the player has to guess a hidden 4-letter word using logical clues.

This project is inspired by the popular word-hunting website HARDWORD and was recreated as a learning project to practice Python programming, game logic, and input validation.

---

## How the Game Works

- The player must guess a hidden 4-letter word.
- The hidden word contains unique letters (no repeated characters).
- The player gets a maximum of **8 attempts** to find the correct word.
- After every guess, the game provides clue points based on letter matching.

---

## Green Points

A green point means:
- The letter exists in the hidden word
- AND it is placed in the correct position

---

## Yellow Points

A yellow point means:
- The letter exists in the hidden word
- BUT it is placed in the wrong position

---

## Example

Suppose the hidden word is:

```text id="qqx5qf"
COLD
```

Player guess:

```text id="dcsl5v"
CODE
```

Result:
- 🟩 `C` → correct letter and correct position
- 🟩 `O` → correct letter and correct position
- 🟨 `D` → present in the word but wrong position

These clues help the player gradually identify the hidden word.

---

## Input Rules

- The player should enter a meaningful 4-letter word.
- Repeated letters are not allowed.

### Exception Handling
The program also includes exception handling to avoid crashes for invalid inputs such as words with incorrect lengths.

This improves the stability and user experience of the game.

---

## Features

- Interactive word-hunting gameplay
- Random word generation
- Green and yellow clue system
- Maximum attempt system
- Input validation and exception handling
- Beginner-friendly game logic

---

## Technologies Used

- Python

---

## Possible Future Improvements

- Score system
- Difficulty levels
- Timer-based gameplay
- Larger word database
- Graphical user interface (GUI)

---

## Author

Developed by Varthyusha Eedammagaari as a beginner Python learning project. 
