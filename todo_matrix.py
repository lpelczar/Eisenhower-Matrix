from datetime import datetime

from todo_quarter import TodoQuarter
from todo_item import TodoItem
from texttable import Texttable

IS_IMPORTANT_IN_LINE_INDEX = 2
TITLE_IN_LINE_INDEX = 0
MINIMAL_QUARTER_TODOITEMS_LENGTH = 0
INDEX_INCREMENTOR = 1
URGENT_HOURS = 72
SECONDS_IN_HOUR = 3600
ACTUAL_YEAR = 2017
DAY_MONTH_INDEX = 1
IMPORTANT_URGENT = 'IU'
IMPORTANT_NOT_URGENT = 'IN'
NOT_IMPORTANT_URGENT = 'NU'
NOT_IMPORTANT_NOT_URGENT = 'NN'
QUOTER_TYPES = (IMPORTANT_URGENT, IMPORTANT_NOT_URGENT, NOT_IMPORTANT_URGENT, NOT_IMPORTANT_NOT_URGENT)
BE_A_DATETIME_OBJECT = 'Incorrect deadline'


class TodoMatrix():
    def __init__(self):
        """
        Constructs a TodoMatrix object with dictionary of all possible quarters
        """
        self.todo_quarters = {}
        for quoter_type in QUOTER_TYPES:
            self.todo_quarters[quoter_type] = TodoQuarter()

    def get_quarter(self, status):
        """
        Returns a chosen TodoQuarter object from a dictionary todo_quarters.
        Status should be one of the possible statuses ('IU', 'IN', 'NU', 'NN').
        :param status: str -> status of TodoQuarter
        :return: TodoQuarter
        """
        return self.todo_quarters.__getitem__(status)

    def add_item(self, title, deadline, is_important=False):
        """
        Adds new item to dictionary todo_quarters using adequate key.
        You should use method add_item from TodoQuarter class.
        Raises TypeError if an argument deadline is not an instance of Datetime class
        :param title: str -> title of task
        :param deadline: DateTime -> deadline of task
        :param is_important: bool -> task importance
        :return: None
        """
        if not isinstance(deadline, datetime):
            raise TypeError(BE_A_DATETIME_OBJECT)
        quoter_type = TodoMatrix.get_item_quoter_type(deadline, is_important)
        self.todo_quarters.get(quoter_type, None).add_item(title, deadline)

    def add_items_from_file(self, file_name):
        """
        Reads data from file_name.csv file and append TodoItem objects to attributes
        todo_items in the properly TodoQuarter objects. Raises FileNotFoundError if a
        file doesn't exist. Every item is written in a separate line the following format:

        title|day-month|is_important

        If is_important is equal to False then last element is en empty string.
        Otherwise the last element is an arbitrary string.
        If the last element of line is an empty string, is_important is equal to False - it means that the
        item should be assign to a not important TODO quarter.
        Otherwise item should be assign to an important TODO quarter.
        """
        try:
            file = open(file_name, 'r')
        except IOError:
            raise FileNotFoundError

        lines = file.read().splitlines()

        for line in lines:
            line = line.split('|')
            title = line[TITLE_IN_LINE_INDEX]
            day, month = line[DAY_MONTH_INDEX].split('-')
            deadline = datetime(ACTUAL_YEAR, int(month), int(day))
            is_important = True if line[IS_IMPORTANT_IN_LINE_INDEX] == 'important' else False
            quarter_name = TodoMatrix.get_item_quoter_type(deadline, is_important)
            self.todo_quarters[quarter_name].todo_items.append(TodoItem(title, deadline))
            self.todo_quarters[quarter_name].sort_items()

        file.close()

    def save_items_to_file(self, file_name):
        """
        Writes all details about TODO items to file_name.csv file
        Every item is written in a separate line the following format:
        title|day-month|is_important
        If is_important contains False then the last element of line should be an empty string.
        Otherwise last element is an arbitrary string.
        :param file_name: str -> name of the file
        :return: None
        """
        content = []
        for k, v in self.todo_quarters.items():
            for i in v.todo_items:
                is_important = 'important' if k in ['IU', 'IN'] else ''
                content.append(i.title + '|' + str(i.deadline.day) + '-' +
                               str(i.deadline.month) + '|' + is_important + '\n')
        with open(file_name, 'w') as f:
            f.write(''.join(content))

    def archive_items(self):
        """
        Removes all TodoItem objects with a parameter is_done set to True from list todo_items
        in every element of dictionary todo_quarters
        :return:
        """
        for k, v in self.todo_quarters.items():
            self.todo_quarters[k].todo_items = [x for x in v.todo_items if not x.is_done]

    def __str__(self):
        """
        Returns a todo_quarters list (an Eisenhower todo_matrix) formatted to string.
        :return: str
        """
        t = Texttable()
        t.add_rows(
            [['', 'URGENT (U)', 'NOT URGENT (N)'],
             ['IMPORTANT (I)', self.get_table_row('IU'), self.get_table_row('IN')],
             ['NOT IMPORTANT (N)', self.get_table_row('NU'), self.get_table_row('NN')]])

        return t.draw()

    @staticmethod
    def get_item_quoter_type(deadline, is_important):
        """
        Returns the type of quoter to which item should be added
        :param deadline: datetime -> deadline of item
        :param is_important: bool -> is task important
        :return: str -> quoter type
        """
        now = datetime.now()
        diff_hours = (deadline - now).total_seconds() / SECONDS_IN_HOUR
        if diff_hours <= URGENT_HOURS and is_important:
            return IMPORTANT_URGENT
        elif diff_hours > URGENT_HOURS and is_important:
            return IMPORTANT_NOT_URGENT
        elif diff_hours <= URGENT_HOURS and not is_important:
            return NOT_IMPORTANT_URGENT
        elif diff_hours > URGENT_HOURS and not is_important:
            return NOT_IMPORTANT_NOT_URGENT

    def get_table_row(self, quoter_type):
        """
        Returns row as string
        :param quoter_type: type of quoter
        :return: str -> string that contains row
        """
        quarter = self.get_quarter(quoter_type)
        output = ''
        if len(quarter.todo_items) == MINIMAL_QUARTER_TODOITEMS_LENGTH:
            return ' '
        else:
            for index, value in enumerate(quarter.todo_items):
                output += str(index + INDEX_INCREMENTOR) + '. ' + str(value) + '\n'
        return output
