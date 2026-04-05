import random  # used to pick random word

# Word lists for different difficulty levels
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

# Welcome message
print("Welcome to the Password Guessing Game 🎮")
print("Choose a difficulty level: easy, medium or hard")

# Take user input
level = input("Enter difficulty: ").lower()

# Select word based on difficulty
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

# Initialize attempt counter
attempts = 0

print("\nGuess the secret password 🔐")

# Game loop runs until user guesses correctly
while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1  # increase attempt count

    # Check if guess is correct
    if guess == secret:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break

    # Generate hint (like Wordle style)
    hint = ""

    # Compare each letter
    for i in range(len(secret)):
        # If letter is correct and in correct position
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"  # incorrect position

    # Show hint to user
    print("Hint:", hint)

# Game ends
print("Game Over ✅")