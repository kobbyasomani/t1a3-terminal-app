from menu import menu_categories
from gamehost import gamehost
from player import player1
from guessing_loop import guessing_loop


def main():
    gamehost.welcome(player1)
    menu_categories.print_menu()
    while menu_categories.selected_category == "":
        menu_categories.prompt_for_selection()
    guessing_loop.start(menu_categories.get_selection())

main()