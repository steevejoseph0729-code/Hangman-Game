
import random

# List of words
words = ["python", "computer", "programming", "developer", "hangman"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of allowed wrong attempts
attempts = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

# Game loop
while attempts > 0:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts left:", attempts)

    # Check if player won
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You won!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess! 👍")
    else:
        attempts -= 1
        print("Wrong guess! ❌")

# Player loses
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)