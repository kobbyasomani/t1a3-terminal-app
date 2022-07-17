import sys
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
        play_again = ""
        while play_again != "y":
            play_again = input(
                "Would you like to play another game (y/n)? ").lower()
            if play_again == "n" or play_again == "no":
                print("\nThanks for playing! Here's how you did:")
                player1.show_player_stats()
                sys.exit(0)
        menu_categories.selected_category = ""


main()
