from datetime import datetime

BE_A_DATETIME_OBJECT = 'Deadline must be a Datetime object'
BE_A_STRING = 'Title must be a string'


class TodoItem():
    def __init__(self, title, deadline):
        """
        Constructs an ToDoItem object Raises ValueError if type of any argument is incorrect
        :param title: str -> task title
        :param deadline: datetime -> task deadline
        """
        if not isinstance(deadline, datetime):
            raise ValueError(BE_A_DATETIME_OBJECT)
        if not isinstance(title, str):
            raise ValueError(BE_A_STRING)
        self.title = title
        self.deadline = deadline
        self.is_done = False

    def mark(self):
        """
        Sets the object's * is_done * attribute to True
        :return: None
        """
        self.is_done = True

    def unmark(self):
        """
        Sets the object's * is_done * attribute to False
        :return: None
        """
        self.is_done = False

    def __str__(self):
        """
        Returns a formatted string with details about todo_item. Format of deadline is 'day-month'
        Expecting output for example done item:
        [x] 12-6 submit assignment
        Expecting output for example undone item:
        [ ] 28-6 submit assignment
        :return: str
        """
        assignment_day = str(self.deadline.day)
        assignment_month = str(self.deadline.month)
        is_assignment_done_char = "x" if self.is_done else " "

        output = "[" + is_assignment_done_char + "]" + " " + assignment_day + "-" + assignment_month + '  ' + self.title

        return output
