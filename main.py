import os

from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


def handle_first_menu_option(TodoMatrix):
    print("1. IT works !")


def handle_second_menu_option(TodoMatrix):
    print("2. IT works !")


def handle_third_menu_option(TodoMatrix):
    print("3. IT works !")


def handle_fourth_menu_option(TodoMatrix):
    print("4. IT works !")


def handle_fifth_menu_option(TodoMatrix):
    print("5. IT works !")


def handle_sixth_menu_option(TodoMatrix):
    print("6. IT works !")


def handle_seventh_menu_option(TodoMatrix):
    print("7. IT works !")


def handle_eighth_menu_option(TodoMatrix):
    print("8. IT works !")


def handle_ninth_menu_option(TodoMatrix):
    print("Thank you for using the program !")
    print(TodoMatrix)
    exit()


OPTIONS = {'1': ['Change status of TODO item', handle_first_menu_option],
           '2': ['Show TODO items sorted decreasing by deadline from chosen quarter', handle_second_menu_option],
           '3': ['Add new TODO task', handle_third_menu_option],
           '4': ['Mark TODO item', handle_fourth_menu_option],
           '5': ['Unmark TODO item', handle_fifth_menu_option],
           '6': ['Remove TODO item', handle_sixth_menu_option],
           '7': ['Archive TODO items', handle_seventh_menu_option],
           '8': ['Show Matrix Table', handle_eighth_menu_option],
           '9': ['Exit program', handle_ninth_menu_option]}


def main():
    todo_matrix = TodoQuarter
    while True:
        for key, value in OPTIONS.items():
            print(key + '. ' + value[0])
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][1](todo_matrix)
            return


if __name__ == "__main__":
    main()
