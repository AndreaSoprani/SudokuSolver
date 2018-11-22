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

        for c in self.cells:
            c.cellsInArcs = self.ComputeCellsInArcs(c.xPos, c.yPos)

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

    def ComputeCellsInArcs(self, xPos, yPos):
        """
        Computes all the cells that are involved in a constraint with the cell at the given coordinates.
        :param xPos: x coordinate of the given cell.
        :param yPos: y coordinate of the given cell.
        :return: a list of all the cells involved in constraints with the given cell.
        """


        output = []

        for c in self.cells:

            # find cells in row
            if c.xPos == xPos and c.yPos != yPos:
                output.append(c)

            # find cells in columns
            if c.yPos == yPos and c.xPos != xPos:
                output.append(c)

            #find cells in 3x3 grid
            if ((c.xPos - 1) // 3 == (xPos - 1) // 3 and (c.yPos - 1) // 3 == (yPos - 1) // 3) \
                    and (c.xPos != xPos or c.yPos != yPos) \
                    and c not in output:
                output.append(c)

        return output