from cell import *

class Grid:
    """
    Class representing a Sudoku grid.

    Attributes:
        cells: a list containing all the cells of the grid.
    """
    cells = []

    def __init__(self):
        """
        Initializes a 9x9 grid of empty cells.
        """
        for j in getValidValueList():
            for i in getValidValueList():
                self.cells.append(Cell(i,j))

    def __str__(self):
        """
        A fancy text representation of a grid.
        """

        output = ""

        for cell in self.cells:

            if cell.xPos == 1:
                output += " "

            output += str(cell) + " "

            if cell.xPos == 3 or cell.xPos == 6:
                output += "|| "

            if cell.xPos == 9:

                output += "\n"

                if cell.yPos == 3 or cell.yPos == 6:
                    output += "-------------------------\n"

        return output