from menu import menu_categories
from gamehost import game_host
from player import player1

def main():
    game_host.welcome(player1)
    menu_categories.print_menu()
    menu_categories.prompt_for_selection()

main()