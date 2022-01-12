<h1 align="center">LHD Build 2022 Sudoku Solver CLI</h1>

# What is LHD Build 2022 Sudoku Solver CLI
## Usage
You can call the program the following way:
```
main.py ${path to sudoku}
```
Where "path to sudoku" is the path to a JSON file containing a 9x9 sudoku in a form of a list of lists.

When using it, you should take into account these points:
- The sudoku solver will solve the sudoku for all its possible solutions. If found, it will show the different solutions by replacing the spaces where multiple number can go with the possible numbers.
- If the sudoku isn't valid from the start, the sudoku solver will return the invalid sudoku.
- If the sudoku isn't valid during a point in the middle of the solving process, the sudoku solver will solve as much as possible from the given sudoku or crash in the attempt.
