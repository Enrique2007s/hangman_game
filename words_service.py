import random
import requests



def get_word():
    """
    Reads a list of words from a words.txt file
    and returns a random word.
    """
    try:
        # checking API for a random word
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()[0].lower()

    except requests.RequestException as e:
        print(f"Error fetching word from API: {e}")

    # If API does not respond, fallback to local words file(words.txt)
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)
    