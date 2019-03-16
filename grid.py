from cell import *
from utility import *
import copy


class Grid:
    """
    Class representing a Sudoku grid.

    Attributes:
        cells: a list containing all the cells of the grid.
    """

    cells = None

    # STANDARD

    def __init__(self):
        """
        Initializes a 9x9 grid of empty cells.
        """
        self.cells = []
        for j in getValidValueList():
            for i in getValidValueList():
                self.cells.append(Cell(i, j))

        for c in self.cells:
            c.arcs = self.ComputeArcs(c.xPos, c.yPos)

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

    def ComputeArcs(self, xPos, yPos):
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

            # find cells in 3x3 grid
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

        for i in range(0, len(values)):
            if values[i] in getValidValueList():
                cell = self.cells[i]
                cell.SetValue(values[i])

    # UTILITY

    def getUnassigned(self):
        output = []

        for cell in self.cells:
            if cell.value is None:
                output.append(cell)

        return output

    def DeadEnd(self):
        """
        Returns true if there's a cell that doesn't admit any value, false otherwise.
        :return: true if a cell has a empty domain, false otherwise.
        """

        return any(len(c.domain) == 0 for c in self.getUnassigned())

    def MRV(self):
        """
        Minimum Remaining Values
        Finds the cell with the smallest domain.
        :return: the cell with the smallest domain.
        """

        cell = next(c for c in self.getUnassigned())

        for c in self.getUnassigned():
            if 1 < len(c.domain) < len(cell.domain):
                cell = c

        return cell

    def Degree(self):
        """
        Finds the cell which is involved in the highest number of constraints on other empty cells.
        :return: the selected cell.
        """
        cell = next(c for c in self.getUnassigned())

        for c in self.getUnassigned():
            if c.GetUnassignedVariablesConstraints() > cell.GetUnassignedVariablesConstraints():
                cell = c

        return cell

    # SOLVE

    def AutoFill(self):
        """
        Used to auto-fill the grid based just on the arcs (immediate constraints).
        :return: the number of cells filled.
        """
        totalfilled = 0

        while True:
            fill = 0

            for cell in self.getUnassigned():
                if cell.AutoFill():
                    fill += 1
                    print("x: " + str(cell.xPos) + ", y: " + str(cell.yPos) + ", val = " + str(cell))
            if fill == 0:
                break

            totalfilled += fill

        return totalfilled

    def Backtracking(self):

        if len(self.getUnassigned()) == 0:
            return True

        deg = self.Degree()
        index = self.cells.index(deg)
        print("x: " + str(deg.xPos) + ", y: " + str(deg.yPos))
        lcv = deg.LCV()
        backup = copy.deepcopy(self)

        while len(lcv) > 0:
            print("x: " + str(deg.xPos) + ", y: " + str(deg.yPos) + ", lcv: " + str(lcv))
            print(deg.value)
            deg.SetValue(lcv.pop(0))
            print(deg.value)
            self.AutoFill()
            if self.DeadEnd():
                print("deadend")
                self = copy.deepcopy(backup)
                deg = self.cells[index]
            elif self.Backtracking() is False:
                print("backtrack false")
                self = copy.deepcopy(backup)
                deg = self.cells[index]
            else:
                return True
        print("false")
        return False