from game import play_game


def main():
    """
    This is the main function that starts the Hangman game.
    """
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have 6 incorrect guesses before you lose.")
    print("Good luck!")
    print("-----------------------------------\n")
    play_game()


if __name__ == "__main__":
    main()