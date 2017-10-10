class TodoMatrix():
    def __init__(self):
        """
        Constructs a TodoMatrix object with dictionary of all possible quarters
        """
        ...

    def get_quarter(self, status):
        """
        Returns a chosen TodoQuarter object from a dictionary todo_quarters.
        Status should be one of the possible statuses ('IU', 'IN', 'NU', 'NN').
        :param status: str -> status of TodoQuarter
        :return: TodoQuarter
        """
        ...

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
        ...

    def add_items_from_file(self, file_name):
        """
        Reads data from file_name.csv file and append TodoItem objects to attributes todo_items in the properly TodoQuarter objects.
        Raises FileNotFoundError if a file doesn't exist. Every item is written in a separate line the following format:
        title|day-month|is_important
        If is_important is equal to False then last element is en empty string. Otherwise the last element is an arbitrary string
        If the last element of line is an empty string, is_important is equal to False - it means that
        the item should be assign to a not important TODO quarter. Otherwise item should be assign to an important TODO quarter.
        :param file_name: str -> name of the file
        :return: None
        """
        ...

    def save_items_to_file(self, file_name):
        """
        Writes all details about TODO items to file_name.csv file Every item is written in a separate line the
        following format:
        title|day-month|is_important
        If is_important contains False then the last element of line should be an empty string.
        Otherwise last element is an arbitrary string.
        :param file_name: str -> name of the file
        :return: None
        """
        ...

    def archive_items(self):
        """
        Removes all TodoItem objects with a parameter is_done set to True from list todo_items in every element of dictionary todo_quarters
        :return:
        """
        ...

    def __str__(self):
        """
        Returns a todo_quarters list (an Eisenhower todo_matrix) formatted to string.
        :return: str
        """
        ...
