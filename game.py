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
    word = get_word()
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        display_word(word, guessed_letters)
        guess = input("Enter a letter: ").lower().strip()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")