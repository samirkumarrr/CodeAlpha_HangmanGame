import tkinter as tk
from tkinter import messagebox
import random

# List of words
words = ["python", "computer", "developer", "keyboard", "programming"]

# Select random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6


def update_display():
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    word_label.config(text=display)
    chances_label.config(
        text=f"Remaining Chances: {max_wrong_guesses - wrong_guesses}"
    )


def guess_letter():
    global wrong_guesses

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning(
            "Invalid Input",
            "Please enter a single alphabet."
        )
        return

    if guess in guessed_letters:
        messagebox.showinfo(
            "Already Guessed",
            "You already guessed this letter."
        )
        return

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1

    update_display()

    # Check win
    won = True
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the word: {word}"
        )
        reset_game()

    # Check lose
    if wrong_guesses >= max_wrong_guesses:
        messagebox.showerror(
            "Game Over",
            f"You lost!\nThe word was: {word}"
        )
        reset_game()


def reset_game():
    global word, guessed_letters, wrong_guesses

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    update_display()


# Main Window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x350")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="HANGMAN GAME",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

word_label = tk.Label(
    root,
    text="",
    font=("Arial", 22)
)
word_label.pack(pady=20)

entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
entry.pack(pady=10)

guess_button = tk.Button(
    root,
    text="Guess Letter",
    font=("Arial", 12),
    command=guess_letter
)
guess_button.pack(pady=10)

chances_label = tk.Label(
    root,
    text="Remaining Chances: 6",
    font=("Arial", 12)
)
chances_label.pack(pady=10)

restart_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 12),
    command=reset_game
)
restart_button.pack(pady=10)

update_display()

root.mainloop()