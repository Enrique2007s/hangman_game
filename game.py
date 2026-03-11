from words_service import get_word

MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    """
    Displays the current state of the word,
    showing guessed letters and underscores for
    unguessed letters.
    """
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nCurrent word: ",  display.strip())


def play_game():
    """
    This function contains the main game loop for Hangman.
    It initializes the game state, handles user input,
    and updates the game state based on the user's guesses.
    """
    word = get_word()
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        display_word(word, guessed_letters)
        guess = input("Enter a letter: ").lower().strip()

# Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue  # Prompt the user to enter a valid letter if the input is
            invalid

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue  # Prompt the user to enter a different letter if they
            have already guessed it

        guessed_letters.append(guess)  # Add the guessed letter to the list of
        guessed letters

        if guess not in word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")
        else:
            print(f"Good guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            return

    print(f"Game over! The word was: {word}")  # Reveal the word if the user
    runs out of attempts or wins the game
