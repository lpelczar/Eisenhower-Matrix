from datetime import datetime
from todo_item import TodoItem


class TodoQuarter():

    def __init__(self):
        """
        Constructs a ToDoQuarter object with list of TodoItem objects
        """
        self.todo_items = []

    def sort_items(self):
        """
        Sorts a todo_items list decreasing by deadline attribute
        """
        self.todo_items.sort(key=lambda x: x.deadline)

    def add_item(self, title, deadline):
        """
        Append TodoItem object to todo_items sorted decreasing by deadline. Raises TypeError
        if an argument deadline is not an instance of Datetime class.
        """
        if not isinstance(deadline, datetime): raise ValueError('Deadline must be a Datetime object')
        self.todo_items.append(TodoItem(title, deadline))
        self.sort_items()

    def remove_item(self, index):
        """
        Removes TodoItem object using index of list todo_items
        """
        self.todo_items.pop(index)
