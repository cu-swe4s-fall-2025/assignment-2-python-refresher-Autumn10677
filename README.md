[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

Implemented `get_columns()` function in `my_utils.py`. This function takes in three mandatory arguments: (1) filename (located in same directory as the Python script), (2) column number to check, and (3) a value to check for in that column. By default, the return in a list of integers containing the file's second column for all matched rows. The returned column can be changed using an optional `result_column` argument, but any non-integer entry found in the result column will throw an error.

`print_fires.py` parses the above arguments before passing them to `get_columns()`.

`run.sh` contains three example usages of `print_fires.py`. The first demonstrates the behavior for a valid call, and the following two examples show the expected behavior when `get_columns()` is given either: (1) an invalid vile name, or (2) a column with any non-integer entries.
