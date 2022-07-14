import random
from menu import menu_categories
from secret import secrets

def guessing_loop():
    # Select a 'secret' at random from the chosen category
    secret = random.choice(secrets[menu_categories.selected_category])
    # print(secret.answer.title())

# menu_categories.selected_category = "mythical creatures"
# guessing_loop()