from cell import *
from utility import *

class Grid:
    """
    Class representing a Sudoku grid.

    Attributes:
        cells: a list containing all the cells of the grid.
    """

    cells = []

    # STANDARD

    def __init__(self):
        """
        Initializes a 9x9 grid of empty cells.
        """
        for j in getValidValueList():
            for i in getValidValueList():
                self.cells.append(Cell(i, j))

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

    # INITIAL SETTING

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

    def SetInitialValues(self, values):
        """
        Sets the initial position of the grid to one given by the values array-
        :param values: array of values for the grid, 0 if the cell is empty.
        """

        for i in range(0,len(values)):
            if values[i] in getValidValueList():
                self.cells[i].SetValue(values[i])

    # UTILITY

    def GridBackup(self):
        """
        Used to backup the grid. It creates a copy of this grid.
        :return: A copy of the grid.
        """

        output = Grid()

        for i in range(0, len(self.cells)):
            output.cells[i].SetValue(self.cells[i].value)

        return output

    def CountFilledCells(self):
        """
        Counts the amount of cells filled in the grid.
        :return: The number of cells filled with a value.
        """

        count = 0
        for cell in self.cells:
            if cell.value is not None:
                count += 1

        return count

    def DeadEnd(self):
        """
        Returns true if there's a cell that doesn't admit any value, false otherwise.
        :return: true if a cell has a empty domain, false otherwise.
        """

        output = False

        for cell in self.cells:
            if len(cell.domain) == 0:
                output = True
                break

        return output

    def MRV(self):
        """
        Minimum Remaining Values
        Finds the cell with the smallest domain.
        :return: the cell with the smallest domain.
        """

        cell = Cell(1, 1)

        for c in self.cells:
            if 1 < len(c.domain) < len(cell.domain):
                cell = c

        return cell


    # SOLVE

    def AutoFill(self):
        """
        Used to auto-fill the grid based just on the arcs (immediate constraints).
        """

        while True:

            fill = 0

            for cell in self.cells:
                if cell.AutoFill():
                    fill += 1

            if fill == 0:
                break
