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
        menu_categories.prompt_for_selection()
        guessing_loop.start(menu_categories.get_selection())
        menu_categories.selected_category = ""

main()
