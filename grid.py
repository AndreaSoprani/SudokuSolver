from cell import *
from utility import *


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
        Initialize a 9x9 grid of empty cells.
        """
        self.cells = []
        for j in get_valid_value_list():
            for i in get_valid_value_list():
                self.cells.append(Cell(i, j))

        for c in self.cells:
            c.arcs = self.compute_arcs(c.xPos, c.yPos)

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

    def compute_arcs(self, x_pos, y_pos):
        """
        Find all the cells that are involved in a constraint with the cell at the given coordinates.
        :param x_pos: x coordinate of the given cell.
        :param y_pos: y coordinate of the given cell.
        :return: a list of all the cells involved in constraints with the given cell.
        """

        output = []

        for c in self.cells:

            # find cells in row
            if c.xPos == x_pos and c.yPos != y_pos:
                output.append(c)

            # find cells in columns
            if c.yPos == y_pos and c.xPos != x_pos:
                output.append(c)

            # find cells in 3x3 grid
            if ((c.xPos - 1) // 3 == (x_pos - 1) // 3 and (c.yPos - 1) // 3 == (y_pos - 1) // 3) \
                    and (c.xPos != x_pos or c.yPos != y_pos) \
                    and c not in output:
                output.append(c)

        return output

    def set_initial_values(self, values):
        """
        Set the initial position of the grid to one given by the values array.
        :param values: array of values for the grid, 0 if the cell is empty.
        """

        for i in range(0, len(values)):
            if values[i] in get_valid_value_list():
                cell = self.cells[i]
                cell.set_value(values[i])

    # UTILITY

    def get_unassigned(self):
        """
        Retrieve a list of all the unassigned cells.
        :return: a list of unassigned cells.
        """
        output = []

        for cell in self.cells:
            if cell.value is None:
                output.append(cell)

        return output

    def dead_end(self):
        """
        Find out if there's a dead end.
        :return: true if a cell has a empty domain, false otherwise.
        """

        return any(len(c.domain) == 0 for c in self.get_unassigned())

    def mrv(self):
        """
        Minimum Remaining Values
        Find the cell with the smallest domain.
        :return: the cell with the smallest domain.
        """

        unassigned = self.get_unassigned()

        cell = unassigned[0]

        for c in unassigned:
            if 1 < len(c.domain) < len(cell.domain):
                cell = c

        return cell

    def degree(self):
        """
        Find the cell which is involved in the highest number of constraints on other empty cells.
        :return: the selected cell.
        """

        unassigned = self.get_unassigned()

        cell = unassigned[0]

        for c in unassigned:
            if c.get_unassigned_variables_constraints() > cell.get_unassigned_variables_constraints():
                cell = c

        return cell

    # SOLVE

    def auto_fill(self):
        """
        Auto-fill the grid based just on the arcs (immediate constraints).
        :return: the number of cells filled.
        """
        total_filled = 0

        while True:
            fill = 0

            for cell in self.get_unassigned():
                if cell.auto_fill():
                    fill += 1
            if fill == 0:
                break

            total_filled += fill

        return total_filled
