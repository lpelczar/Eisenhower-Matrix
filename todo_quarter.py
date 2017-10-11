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

    def archive_items(self):
        """
        Removes all TodoItem objects with a parameter is_done set to True from list todo_items.
        """
        self.todo_items = [x for x in self.todo_items if not x.is_done]

    def get_item(self, index):
        """
        Returns TodoItem object from index of list todo_items. Raises IndexError if an argument
        index is out of range list todo_items.
        """
        return self.todo_items[index]

    def __str__(self):
        """
        Returns a formatted list of todo_items sorted decreasing by deadline.
        There is an expecting output:
        1. [ ] 9-6 go to the doctor 2. [x] 11-6 submit assignment
        Hint: use instance method str() from class TodoItem
        """
        self.sort_items()
        return ''.join([str(k + 1) + '. ' + str(v) + ';' for k, v in enumerate(self.todo_items)])
