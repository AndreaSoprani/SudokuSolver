# SudokuCSP
###### by Andrea Soprani

This solver uses CSP (Constraint Satisfaction Problem) algorithms to solve sudokus.<br/>

+ Cells hold a value (the variable).
+ The domain is represented by the possible values for an unfilled cell.
+ Each cell is in a constraint with a cell on the same row, column or sub-grid.

Node and Arc consistency are checked when setting a value in a cell:
+ A value can be set only if the value is in the domain (node-consistency).
+ When a value is set in a cell, the value is removed from the domain of the cells in the same row, column or sub-grid 
(arc-consistency).

The algorithm solves the sudoku through backtracking (dfs).
Variable selection can be done with 2 policies:
 * MRV (Minimum Remaining Values) (default)
 * Degree
 
Value selection is done with the LCV (Least Constraining Value) policy.

## Instructions

Sudokus to be solved are stored in "sudokus.txt".
Each sudoku must be stored in a line of 81 characters in the range [0, 9] (0 for empty cells, 1-9 for filled ones).
No blank lines should be included in this file.
This file already contains 10 difficult sudokus.

Solved sudokus will be stored in "solutions.txt".
The file will show solution time, unsolved grid and solved grid for each sudoku in "sudokus.txt" and it will be overwritten 
at each execution of "main.py".

Execute "main.py" in order to solve all the sudokus in "sudokus.txt".