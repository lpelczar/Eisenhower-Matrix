# The Eisenhower Matrix App

## The story

The Eisenhower Matrix is a great tool for time managing and improve your productivity. It is often used in IT projects teams to prioritize tasks.

Bob is a beginner Codecooler. He is a good self-learner, but he has a problem to focus on the only one thing in one moment. That's the reason that he sometimes feels lost in his job. Please help him to improve his efficiency and implement for him Eisenhower Matrix Application. He precised his expectations the user story.

## Tasks

1. Important & urgent: Implement all modules described in a specification.
2. Important & not urgent: Adjust it for user needs, based on the user story.
3. Not important & urgent: Fill up the specification (use markdown syntax).
4. Not important & not urgent: Add some extra features.


## The user story

1. As a user I would like to choose a status of shown TODO items:

  - urgent & important items
  - not urgent & important items
  - urgent & not important items
  - not urgent & not important items

    Urgent means that there's 3 days (72 hours) to deadline at most.

2. As a user I would like to see a list TODO items sorted decreasing by deadline from chosen matrix's quarter with its details.

3. As a user I would like to see a deadline formatted to *day-month*. I use matrix for the 2017 year.

4. As a user I would like to add an item with its deadline and priority, which is automatically assign to a properly quarter.

5. As a user I would like to mark TODO item by cross if it's done.

6. As a user I would like to undo marking a TODO item.

7. As a user I would like to remove a chosen TODO item.

8. As a user I would like to archive TODO items - remove all done items.

9. As a user I would like to keep all my TODO items in a .csv files.

10. As a user I would like to automatically archive all done tasks before save items and quit the application.

11. As a user I would like to see a whole Eisenhower matrix (every quarter with its items).

### Extras:

12. As a user I would like to see colored (only unmarked) todo_items:
  - green: if the deadline is coming far than 3 days
  - orange: if deadline is coming in the next 3 days
  - red: if deadline is today

13. As a user I would like to see a matrix formatted to the following table.

```
"
    |            URGENT              |           NOT URGENT           |  
  --|--------------------------------|--------------------------------|--
    | 1. [ ] 9-6  go to the doctor   |                                |
    | 2. [x] 11-6 submit assignment  |                                |
  I |                                |                                |
  M |                                |                                |
  P |                                |                                |
  O |                                |                                |
  R |                                |                                |      
  T |                                |                                |
  A |                                |                                |
  N |                                |                                |
  T |                                |                                |
    |                                |                                |
    |                                |                                |
  --|--------------------------------|--------------------------------|--                               
  N | 1. [ ] 14-6 buy a ticket       | 1. [x] 30-5 House of Cards     |
  O |                                |                                |
  T |                                |                                |
    |                                |                                |
  I |                                |                                |
  P |                                |                                |
  O |                                |                                |
  R |                                |                                |
  T |                                |                                |
  A |                                |                                |
  N |                                |                                |
  T |                                |                                |
  --|--------------------------------|--------------------------------|--
  "
  ```


## Requirements

* Implement all modules described in a specification.

* Implement the *main.py* module and fulfill its specification.

* You are allowed to implement your own custom functions and modules. Remember about clean code.

* All tests must pass.

* Please don't change a file *todo_items_read_test.csv*! It's important for passing tests.

* Your program should fulfill cases described in the user story.

* Use module *datetime* for time variables and operations -> https://docs.python.org/3/library/datetime.html

* Program should be based on the Object Oriented Programming paradigm

* Remember about proper constructors - not all attributes object are assign by a parameter!

* Plan your task in Eisenhower matrix. First of all focus on the implement required class (and its instance methods). Then think about usefulness.

* Please fill up specification in this file if you implemented more functions. Use markdown syntaxes.


## The specification

### `main.py`

__Functions__

* `get_color_of_todo_item(TodoItem)`

  Function returns color based on TodoItem deadline.

* `handle_first_menu_option(TodoMatrix)`

  Lists tasks of selected quarter by deadline.

* `handle_second_menu_option(TodoMatrix)`  

  Adds new task

* `handle_third_menu_option(TodoMatrix)`

  Mark chosen TodoItem as done.

* `handle_fourth_menu_option(TodoMatrix)`

  Unmark chosen TodoItem.

* `handle_fifth_menu_option(TodoMatrix)`

  Removes TodoItem.

* `handle_sixth_menu_option(TodoMatrix)`

  Archives all marked TodoItems.

* `handle_seventh_menu_option(TodoMatrix)`  

  Prints formatted matrix table.

* `handle_eighth_menu_option(TodoMatrix)`

  Close the program, archive all TodoItems and save unsaved data.

* `main()`

  Handle menu.


### `todo_item.py`

This is the file containing a todo_item logic.

### Class TodoItem

__Attributes__

* `title`
  - data: string
  - description: title of todo_item

* `deadline`
  - data: Datetime object
  - description: deadline of todo_item, year is always set to *2017*

* `is_done`
  - data: bool
  - description: contains True if TODO item is done, otherwise contains False.  Default value is False

__Instance methods__

* ##### ` __init__(self, title, deadline)`

  Constructs an ToDoItem object
  Raises ValueError if type of any argument is incorrect

* `mark(self)`

  Sets the object's * is_done * attribute to True

* `unmark(self)`

  Sets the object's * is_done * attribute to False

* `__str__(self)`

  Returns a formatted string with details about todo_item.
  Format of deadline is 'day-month'

  Expecting output for example done item:

  `[x] 12-6 submit assignment`

  Expecting output for example undone item:

  `[ ] 28-6 submit assignment`

### `todo_quarter.py`

This is the file containing a logic of an Eisenhower todo_quarter.

### Class TodoQuarter

__Instance Attributes__

* `todo_items`
  - data: list
  - description: list of TodoItem objects

__Instance methods__

* ##### ` __init__(self) `

  Constructs a *ToDoQuarter* object with list of TodoItem objects

* `sort_items(self)`

  Sorts a *todo_items* list decreasing by *deadline* attribute

* `add_item(self, title, deadline)`

  Append *TodoItem* object to *todo_items* sorted decreasing by *deadline*.
  Raises *TypeError* if an argument *deadline* is not an instance of Datetime class.

* `remove_item(self, index)`

  Removes *TodoItem* object using *index* of list *todo_items*

* `archive_items(self)`

  Removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items*.

* `get_item(self, index)`

  Returns *TodoItem* object from *index* of list *todo_items*.
  Raises *IndexError* if an argument *index*  is out of range list *todo_items*.

* `__str__(self)`

  Returns a formatted list of *todo_items* sorted decreasing by *deadline*. There is an expecting output:

  `1. [ ] 9-6  go to the doctor
   2. [x] 11-6 submit assignment`

  Hint: use instance method *__str__()* from class *TodoItem*


### `todo_matrix.py`
### Class TodoMatrix

This is the file containing the logic of an Eisenhower todo_matrix.

__Attributes__

* `todo_quarters`

  - data: dictionary
  - description: contains *TodoQuarter* objects

    key: string - status of todo_quarter, value: ToDoQuarter object

        possible keys of TODO quarter:
        - 'IU' means that todo_quarter contains important todo_items & urgent
        - 'IN' means that todo_quarter contains important todo_items & not urgent
        - 'NU' means that todo_quarter contains not important todo_items & urgent
        - 'NN' means that todo_quarter contains not important & not urgent todo_items


__Instance methods__

* ##### `__init__(self) `

  Constructs a *TodoMatrix* object with dictionary of all possible quarters

* `get_quarter(self, status)`

  Returns a chosen *TodoQuarter* object from a dictionary *todo_quarters*.
  Status should be one of the possible statuses ('IU', 'IN', 'NU', 'NN').

* `add_item(self, title, deadline, is_important=False)`

  Adds new item to dictionary *todo_quarters* using adequate key. You should use method *add_item* from *TodoQuarter* class.

  Raises *TypeError* if an argument *deadline* is not an instance of Datetime class.

* `add_items_from_file(self, file_name)`

  Reads data from *file_name.csv* file and append *TodoItem* objects to attributes *todo_items* in the properly *TodoQuarter*   objects.
  Raises *FileNotFoundError* if a file doesn't exist.
  Every item is written in a separate line the following format:

  `title|day-month|is_important`

  If *is_important* is equal to False then last element is en empty string. Otherwise the last element is an arbitrary string
  If the last element of line is an empty string, *is_important* is equal to False - it means that the item should be assign     to a not important TODO quarter. Otherwise item should be assign to an important TODO quarter.

* `save_items_to_file(self, file_name)`

  Writes all details about TODO items to *file_name.csv* file
  Every item is written in a separate line the following format:

  `title|day-month|is_important`

  If *is_important* contains False then the last element of line should be an empty string. Otherwise last element is an         arbitrary string.

* `archive_items(self)`

  Removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items* in every element of dictionary *todo_quarters*

* `__str__(self)`

  Returns a todo_quarters list (an Eisenhower todo_matrix) formatted to string.

* `get_item_quoter_type(deadline, is_important)`

  Returns the type of quoter to which item should be added. This method should be static method.

* `get_table_row(self, quoter_type)`

  Returns row of a table as a string.