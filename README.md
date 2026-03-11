# Hangman Game

Welcome to Hangman Game! A python based terminal game which runs on Heroku. 

Users try to guess the word before they run out of guesses. There are 6 guesses in total each game and the word can be as long as it can be short.

## How To Play!

In each game, you have 6 incorrect guesses before you lose. Each time you enter a letter, depending whether it was right or not, will be placed on a blank space or will tell you you have gotten it wrong.

If you guess all the letters correctly, you win! If not, you lose.

## Features

1-) Random word generation
Words are not always the same thanks to an API used to generate random words.
If the API fails, there is a list of 20 words where the PC can chose randomly for the player.

<img width="384" height="207" alt="image" src="https://github.com/user-attachments/assets/172a3862-8bba-4995-a75c-7b0c076918ff" />

2-) Input Validation and error-checking
You cannot enter repeated letters, numbers, or words. If you add a space, it will be automatically removed.

<img width="369" height="283" alt="image" src="https://github.com/user-attachments/assets/3eb19abf-e254-40e0-97ae-622864e339e3" />
<img width="237" height="116" alt="image" src="https://github.com/user-attachments/assets/a582bcad-5d55-49e5-9199-167d6e9fa956" />

3-) Model

I decided to keep it simple and create a method (display_word) where the letters are covered, when guessed, they uncover.
This area accomodates for however big or small the word is.
It has print methods to print the current amount of letters guessed/covered, as well as whether you guessed the letter right or not.

## Testing

I have manually tested the project by doing the following:

Made sure all errors were given correct try statements.

### pep8 Testing

game.py
<img width="1087" height="799" alt="image" src="https://github.com/user-attachments/assets/62f45d21-ab63-44d6-9884-d05ab92e9482" />

main.py
<img width="1169" height="776" alt="image" src="https://github.com/user-attachments/assets/04a6ee31-eb3b-4e4a-8afa-37c41735fe6d" />

words_service.py
<img width="1199" height="729" alt="image" src="https://github.com/user-attachments/assets/74ad9305-f08b-48ed-8ac6-58dc28539921" />


## Bugs
No known bugs found.

## Validator Testing

As shown before, no erors were shown in the CodeInstitute Python Linter.

# Deployment

Successfully deployed to Github. Heroku is still a problem.


#Credits

ChatGPT for suggestions on various projects to create
Copilot in VS Code suggesting code suggestions
DeepSeek helped when I got stuck and did not know how to continue. Used in areas of doubt such as words_service.py script.
