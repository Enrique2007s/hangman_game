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

Had other people try to break the game(unsuccessfully)

### Validator Testing

game.py
<img width="1087" height="799" alt="image" src="https://github.com/user-attachments/assets/62f45d21-ab63-44d6-9884-d05ab92e9482" />

main.py
<img width="1169" height="776" alt="image" src="https://github.com/user-attachments/assets/04a6ee31-eb3b-4e4a-8afa-37c41735fe6d" />

words_service.py
<img width="1199" height="729" alt="image" src="https://github.com/user-attachments/assets/74ad9305-f08b-48ed-8ac6-58dc28539921" />


## Bugs
No known bugs found.

# Deployment

Successfully deployed to Github. Successfully deployed to Heroku.
Heroku was a nightmare, so much so that I needed help from one of my developer mates. 

# Credits

ChatGPT for suggestions on various projects to create
Copilot in VS Code suggesting code suggestions
DeepSeek helped when I got stuck and did not know how to continue. Used in areas of doubt such as words_service.py script. Furthermore, DeepSeek helped me try to deploy my project to Heroku... Unsuccessfuly
CodeInstitute Linter to confirm all Python code was correct
Youtube had a great role in helping me determine how to create the project and what I could be able to accumplish wiht just Python

My mother because she asked me to be included in the README.md. She has been a great help in terms or moral support and without her, I would not have been so optimistic in creeating this project

## Notes
The project was turned in late. The reason for this is because I had no idea how to deploy to Heroku, even with Tutor support, it was difficult to understand what they meant. I apologise for this unprofessional action. 

## What I have learnt

I have learnt that it is always okay to ask for help. There is no shame in being unknowledgeable about something, the real shame is in staying unknowledgeable.

Lastly, in the notes from the assessor, I would like to know if this project had not been turned in late, what grade I would have gotten(pass, merit, or distinction).


