import sys
from os import system
from menu import menu_categories
from gamehost import gamehost
from player import player1
from guessing_loop import guessing_loop


def main():
    while menu_categories.selected_category == "":
        # Show player stats above the menu when at least one game has been played
        player1.show_player_stats()
        gamehost.welcome(player1.get("games_played"))
        menu_categories.print_menu()
        gamehost.intro_category(menu_categories.prompt_for_selection())
        guessing_loop.start(menu_categories.get_selection())
        keep_playing = gamehost.give_choice(
            "Would you like to play another game")
        if keep_playing == True and keep_playing != "quit":
            menu_categories.selected_category = ""
            system("clear")
        else:
            system("clear")
            gamehost.goodbye(player1.get("games_played"))
            player1.show_player_stats()
            sys.exit(0)


main()
