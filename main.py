from gamehost import game_host
from player import player1
import guessing_loop

def main():
    game_host.welcome(player1)
    guessing_loop.menu_categories.print_menu()
    guessing_loop.menu_categories.prompt_for_selection()
    guessing_loop.guessing_loop()

main()