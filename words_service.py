import random

def get_word():
    """
    Reads a list of words from a words.txt file
    and returns a random word.
    """
    with open("words.txt" , "r") as file:
        words = file.read().splitlines()
    return random.choice(words)