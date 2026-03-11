import random
import requests

API_URL = "https://random-word-api.herokuapp.com/word?number=1"


def get_word():
    """
    Reads a list of words from a words.txt file
    and returns a random word.
    """
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()[0]
    except requests.RequestException as e:
        print(f"Error fetching word from API: {e}")

    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)