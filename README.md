# SudokuCSP
##### by Andrea Soprani

This solver uses CSP (Constraint Satisfaction Problem) algorithms to solve sudokus.<br/>

+ Cells hold a value (the variable).
+ The domain is represented by the possible values for an unfilled cell.
+ Each cell is in a constraint with a cell on the same row, column or sub-grid.

Node and Arc consistency are checked when setting a value in a cell:
+ A value can be set only if the value is in the domain (node-consistency).
+ When a value is set in a cell, the value is removed from the domain of the cells in the same row, column or sub-grid 
(arc-consistency).
