import sys
from os import system
from menu import menu_categories
from gamehost import gamehost
from player import player1
from guessing_loop import guessing_loop


def main():
    """The main game loop"""
    while menu_categories.selected_category == "":
        # Show player stats above the menu when game has been played > 0
        player1.show_player_stats()
        # Print welcome message
        gamehost.welcome(player1.get("games_played"))
        # Print menu and and get intro message for chosen category
        menu_categories.print_menu()
        gamehost.intro_category(menu_categories.prompt_for_selection())
        # Start guessing loop
        guessing_loop.start(menu_categories.get_selection())
        # Ask if player wants to continue after game round
        keep_playing = gamehost.give_choice(
            "Would you like to play another game")
        # If yes, clear category and restart loop
        if keep_playing == True and keep_playing != "quit":
            menu_categories.selected_category = ""
            system("clear")
        # Else, quit the program
        else:
            system("clear")
            gamehost.goodbye(player1.get("games_played"))
            player1.show_player_stats()
            sys.exit(0)


main()
