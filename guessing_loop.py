import random
from menu import menu_categories
from secret import secrets

def guessing_loop():
    #Select a 'secret' at random from the chosen category
    secret = random.choice(secrets[menu_categories.selected_category])
    # print(secret.answer.title())

    # present a clue to the user and take input

    # update remaining and used guesses

    # decrement remaining guesses if the guess does not match the secret

    # give feedback after each guess

    # end the loop if the guess matches the secret

    # update overall user stats at the end of the guessing round

    # update menu at the end of the guessing round (show stats at the top)

# menu_categories.selected_category = "mythical creatures"
# guessing_loop()

