<h1 align="center">LHD Build 2022 Sudoku Solver CLI</h1>

# What is LHD Build 2022 Sudoku Solver CLI?
LHD Build 2022 Sudoku Solver CLI is a sudoku solver built for the "Build a sudoku solver" LHD: Build 2022's challenge.

## Dependencies
- Python.

## Platform
- Cross-platform.

## Usage
You can call the program the following way:
```
main.py ${path to sudoku}
```
Where "path to sudoku" is the path to a JSON file containing a 9x9 sudoku in a form of a list of lists.

Internally, the sudoku solver will return the following:
- If the sudoku is valid and has only 1 solution, the sudoku solver will return the only solution.
- If the sudoku is valid and has multiple solutions, the sudoku solver will solve the sudoku for all its possible solutions and show them by replacing the content of the squares where multiple number can go with a list containing the possible numbers.
- If the sudoku isn't valid from the start, the sudoku solver will return the invalid sudoku.
- If the sudoku isn't valid during a point in the middle of the solving process, the sudoku solver will solve as much as possible from the given sudoku and return it or crash in the attempt.

The CLI prints the return value of the internal sudoku solver.

## License
All the code owned in this repository is under the [MIT License](https://github.com/GaryNLOL/lhdbuild2022-sudoku-solver-cli/blob/main/LICENSE).
