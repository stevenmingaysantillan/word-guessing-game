Description:

A puzzle game where the user tries to guess a hidden secret word. The program acts as an interactive word matrix, providing real-time capital and lowercase letter hints to guide the player to the correct answer.

Key Features
Dynamic Hint Generator: Compares the player's guess to the secret word index-by-index. It outputs an UPPERCASE letter if the character is in the perfect spot, a lowercase letter if the character is in the word but in the wrong spot, and an underscore (_) if it doesn't match.

Input Validation & Safety: Checks the string length (len()) of the user's guess against the secret word length, warning the player if their guess is invalid without wasting a turn.

Game Loop & Score Tracking: Implements a while loop that keeps the game alive until the correct word is typed, automatically tracking and displaying the total guess count upon victory.
