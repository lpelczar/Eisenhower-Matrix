import os

from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix

ITEMS_CSV_FILE_PATH = 'todo_items.csv'
QUARTERS = ['IU', 'IN', 'NU', 'NN']


# Kamil
def handle_first_menu_option(TodoMatrix):
    print("1. IT works !")


#Kamil
def handle_second_menu_option(TodoMatrix):
    print("2. IT works !")


#Kamil
def handle_third_menu_option(TodoMatrix):
    print("3. IT works !")


def handle_fourth_menu_option(TodoMatrix):
    """
    Mark chosen TodoItem as done.
    :param TodoMatrix: TodoMatrix
    :return: none
    """
    while True:
        quarter_name = input('Enter quarter name (IU, IN, NU, NN): ')
        if quarter_name not in QUARTERS:
            print('Wrong quarter! ', end='')
            continue
        item_number = input('Enter item number to mark it: ')
        if item_number not in [str(x) for x in range(1, len(TodoMatrix.todo_quarters[quarter_name].todo_items) + 1)]:
            print('Wrong number! ', end='')
            continue
        break
    TodoMatrix.todo_quarters[quarter_name].todo_items[int(item_number) - 1].mark()


def handle_fifth_menu_option(TodoMatrix):
    """
    Unmark chosen TodoItem.
    :param TodoMatrix: TodoMatrix
    :return: none
    """
    while True:
        quarter_name = input('Enter quarter name (IU, IN, NU, NN): ')
        if quarter_name not in QUARTERS:
            print('Wrong quarter! ', end='')
            continue
        item_number = input('Enter item number to unmark it: ')
        if item_number not in [str(x) for x in range(1, len(TodoMatrix.todo_quarters[quarter_name].todo_items) + 1)]:
            print('Wrong number! ', end='')
            continue
        break
    TodoMatrix.todo_quarters[quarter_name].todo_items[int(item_number) - 1].unmark()


#Łukasz Remove Todo Item
def handle_sixth_menu_option(TodoMatrix):
    print("6. IT works !")


#done
def handle_seventh_menu_option(TodoMatrix):
    TodoMatrix.archive_items()
    print("7. Items have been archived")


#done
def handle_eighth_menu_option(TodoMatrix):
    print(TodoMatrix)

#done
def handle_ninth_menu_option(TodoMatrix):
    print("Thank you for using the program !")
    TodoMatrix.archive_items()
    TodoMatrix.save_items_to_file(ITEMS_CSV_FILE_PATH)
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
    todo_matrix = TodoMatrix()
    todo_matrix.add_items_from_file(ITEMS_CSV_FILE_PATH)
    while True:
        for key, value in OPTIONS.items():
            print(key + '. ' + value[0])
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][1](todo_matrix)


if __name__ == "__main__":
    main()
