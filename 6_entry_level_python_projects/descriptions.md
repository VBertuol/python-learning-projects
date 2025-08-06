# Python Essential Projects: Progressive Challenges

This document presents a sequence of Python projects, from beginner to intermediate level, designed to practice core language concepts (variables, basic types, control structures, functions, lists, dictionaries, and file I/O) without using external libraries.

Each project includes:

* **Objective**: what the project should accomplish.
* **Requirements**: minimum features to implement.
* **Optional Challenges**: extensions to deepen learning.
* **Key Concepts**: Python topics to master.

---

## Project 1: Simple Calculator

### Objective

Build a calculator that takes two numbers and an operator (+, -, \*, /) from the user and displays the result.

### Requirements

* Read two numeric values from the user.
* Read the desired operator.
* Validate division by zero.
* Display the formatted result.
* Allow repeating calculations until the user types “exit.”

### Optional Challenges

* Support additional operators (%, \*\*).
* Handle invalid inputs (letters, unknown symbols).

### Key Concepts

* `input()` and type conversion (`int()`, `float()`).
* Conditionals (`if`/`elif`/`else`).
* `while` loops.
* Basic error handling with `try`/`except`.

---

## Project 2: Guess the Number

### Objective

Create a game where the program picks a random number between 1 and 100, and the user tries to guess it.

### Requirements

* Generate a random number using `randrange`.
* Read user guesses until the correct number is guessed.
* Indicate if the guess is too high or too low.
* Count the number of attempts.

### Optional Challenges

* Allow the user to choose the range (e.g., 1–1000).
* Implement difficulty levels (fewer attempts, hints).

### Key Concepts

* Importing modules (`from random import randrange`).
* `while` loops.
* Counters and state variables.

---

## Project 3: FizzBuzz CLI

### Objective

Implement the classic FizzBuzz challenge in Python, printing numbers from 1 to N on the command line.

### Requirements

* Read an integer N from the user.
* For each number from 1 to N:
    * Print “Fizz” if it is a multiple of 3.
    * Print “Buzz” if it is a multiple of 5.
    * Print “FizzBuzz” if it is a multiple of both 3 and 5.
    * Otherwise, print the number itself.

### Optional Challenges

* Validate that N is positive.
* Display output in columns or add colors using ANSI escape codes.

### Key Concepts

* `for` loops with `range()`.
* Modulo operator (`%`).
* Chained conditionals.

---

## Project 4: To-Do List Manager

### Objective

Implement a simple in-memory task manager.

### Requirements

* Interactive menu: add, list, and remove tasks.
* Store tasks in a list of dictionaries (each task has an ID, description, and status).
* Update task status (pending/completed).

### Optional Challenges

* Persist tasks to a text file (read/write JSON or CSV).
* Implement keyword search.

### Key Concepts

* Lists and dictionaries.
* Functions for each action (add, list, remove).
* File I/O.
* Parsing JSON or CSV using built-in modules (`json` or `csv`).

---

## Project 5: Hangman Game

### Objective

Create a Hangman game where the user guesses a word letter by letter.

### Requirements

* Define a fixed list of words in the code.
* Select one word at random.
* Display progress (e.g., `_ A _ A _`).
* Limit the number of attempts.
* Show letters already guessed.

### Optional Challenges

* Read words from an external text file.
* Provide hints (show category or brief description).

### Key Concepts

* String manipulation.
* Sets (`set`) to track used letters.
* Main loop with win/lose conditions.

---

## Project 6: Store Inventory CLI

### Objective

Build a CLI to register, list, and update products, saving data to a text file.

### Requirements

* Each product: code, name, quantity, and price.
* Menu options: add, list all, search by code, and remove.
* Persist data in a CSV or simple text file.
* Load data at startup and save on exit.

### Optional Challenges

* Validate numeric formats when reading from the file.
* Implement quantity updates (inventory management).
* Sort the listing by name or price.

### Key Concepts

* File I/O (`open`, `read`, `write`).
* Splitting and joining strings.
* Exception handling when reading files.

---

## How to Progress

* Complete each project fully before moving to the next one.
* Read the official Python documentation (docs.python.org) to reinforce syntax and built-in functions.
* Refactor your code: extract helper functions, improve variable names, and add comments.
* Share your code on GitHub and seek feedback.

Happy coding and learning!