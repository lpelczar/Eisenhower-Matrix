import os


from todo_matrix import TodoMatrix
import todo_matrix
from datetime import datetime

METHOD_INDEX = 1

DESCRIPTION_INDEX = 0

SECONDS_IN_HOUR = 3600

ITEMS_CSV_FILE_PATH = 'todo_items.csv'
QUARTERS = ['IU', 'IN', 'NU', 'NN']

# Colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
WHITE = '\033[37m'
BOLD_GREEN = '\033[1;32m'
UNDERLINE = '\033[4m'


def get_color_of_todo_item(TodoItem):
    """
    Function returns color based on TodoItem deadline
    :param TodoItem: TodoItem
    :return: str -> ascii color node
    """
    if TodoItem.is_done:
        return WHITE
    deadline = TodoItem.deadline
    now = datetime.now()
    diff_hours = (deadline - now).total_seconds() / SECONDS_IN_HOUR
    if diff_hours > 72:
        return BOLD_GREEN
    elif diff_hours == 0:
        return WARNING
    else:
        return FAIL



def handle_second_menu_option(TodoMatrix):
    """
    Lists tasks of selected quarter by deadline
    :param TodoMatrix: TodoItem
    :return: None
    """
    quarters = ','.join(todo_matrix.QUOTER_TYPES)
    user_input = input('Chose one of the following quarters ' + quarters + " : ")
    if user_input not in todo_matrix.QUOTER_TYPES:
        print('\n' + FAIL + "Bad quoter type" + ENDC)
    else:
        quarter = TodoMatrix.get_quarter(user_input)
        if len(quarter.todo_items) == 0:
            print('\n' + WARNING + 'The quater is empty !' + ENDC)
        else:
            for index, value in enumerate(quarter.todo_items):
                if (not value.is_done):
                    print(get_color_of_todo_item(value) + str(index + 1) + '. ' + str(value) + ENDC)
                else:
                    print(str(index + 1) + '. ' + str(value))

    print()



def handle_third_menu_option(TodoMatrix):
    """
    Adds new task
    :param TodoMatrix: TodoItem
    :return: None
    """
    user_input = input('Type information in the following syntax: \n<day>,<month>,<title><is important>'
                       + ' (i.e: 17,11,new task,true): ')
    task_information = user_input.split(',')
    try:
        deadline = datetime(2017, int(task_information[1]), int(task_information[0]))
        title = task_information[2]
        is_important = bool(task_information[3])
        TodoMatrix.add_item(title, deadline, is_important)
        TodoMatrix.save_items_to_file(ITEMS_CSV_FILE_PATH)
        print(OKGREEN + "\nSuccessfuly added new task !\n" + ENDC)
    except:
        print('\n' + FAIL + "Your input is wrong or this task already exists !" + ENDC + '\n')


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


def handle_sixth_menu_option(TodoMatrix):
    """
    Removes TodoItem.
    :param TodoMatrix: TodoMatrix
    :return: none
    """
    while True:
        quarter_name = input('Enter quarter name (IU, IN, NU, NN): ')
        if quarter_name not in QUARTERS:
            print('Wrong quarter! ', end='')
            continue
        item_number = input('Enter item number to remove: ')
        if item_number not in [str(x) for x in range(1, len(TodoMatrix.todo_quarters[quarter_name].todo_items) + 1)]:
            print('Wrong number! ', end='')
            continue
        break
    TodoMatrix.todo_quarters[quarter_name].remove_item(int(item_number) - 1)


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


OPTIONS = {
    '1': ['Show TODO items sorted decreasing by deadline from chosen quarter', handle_second_menu_option],
    '2': ['Add new TODO task', handle_third_menu_option],
    '3': ['Mark TODO item', handle_fourth_menu_option],
    '4': ['Unmark TODO item', handle_fifth_menu_option],
    '5': ['Remove TODO item', handle_sixth_menu_option],
    '6': ['Archive TODO items', handle_seventh_menu_option],
    '7': ['Show Matrix Table', handle_eighth_menu_option],
    '8': ['Exit program', handle_ninth_menu_option]}


def main():
    todo_matrix = TodoMatrix()
    todo_matrix.add_items_from_file(ITEMS_CSV_FILE_PATH)
    while True:
        for key, value in OPTIONS.items():
            print(OKGREEN + key + '. ' + value[DESCRIPTION_INDEX] + ENDC)
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('clear')
        else:
            os.system('clear')
            OPTIONS[user_input][METHOD_INDEX](todo_matrix)


if __name__ == "__main__":
    main()
