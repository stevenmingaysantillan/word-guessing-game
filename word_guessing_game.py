"""
Good day! This is my project, this time I only added a small
hint at the beginning, and I also wanted to add the keep playing function but I don't know
how to put random words as same as random randint.
"""

secret_word = "building"

guess_count = 0
guesses = -1 

print()

print("Welcome to the word guessing game!")
print("Hint: It's a place where people mostly spend their money with their friends and family.")

print()

initial_hint = ""
for letter in secret_word:
    initial_hint += "_ "
print(f"Your hint is: {initial_hint}")

while guesses != secret_word:
    guesses = input("What is your guess? ").lower()
    guess_count = guess_count + 1
    if len(guesses) != len(secret_word):
        print("Your guess must be the same length as the secret word.")

    else:
        hint = ""
        for i in range(len(secret_word)):
            if guesses[i] == secret_word[i]:
                hint += guesses[i].upper() + " "

            elif guesses[i] in secret_word:
                hint += guesses[i].lower() + " "
            
            else:
                hint += "_ "

        if guesses != secret_word:
            print(f"Your hint is: {hint}")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses!")