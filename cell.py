from utility import *


class Cell:
    """
    A class representing a Sudoku cell.

    Attributes:
        xPos: the x position of the cell (from 1 to 9).
        yPos: the y position of the cell (from 1 to 9).
        value: the value assigned to the cell. None if no value is assigned yet.
        domain: a list containing all the possible assignment to the cell.
            Only values between 1 and 9 are allowed.
            If a value is assigned to the cell it must contain only that value.
    """
    xPos = None
    yPos = None
    value = None
    domain = None
    arcs = None

    def __init__(self, x_pos, y_pos):
        """
        Initialize an empty cell in a given position.
        :param x_pos: the x position of the cell (from 1 to 9).
        :param y_pos: the y position of the cell (from 1 to 9).
        """

        if x_pos not in get_valid_value_list():
            raise InvalidPosition("xPos", x_pos)
        if y_pos not in get_valid_value_list():
            raise InvalidPosition("yPos", y_pos)

        self.xPos = x_pos
        self.yPos = y_pos
        self.domain = get_valid_value_list()
        self.arcs = []

    def __str__(self):
        """
        String representation of the cell.
        :return: the value as a string. If the value is None returns a whitespace.
        """
        if self.value is None:
            return " "
        return str(self.value)

    def set_value(self, value):
        """
        Set the value of the cell to a given value.
        The setting is performed only if the previous value is None and the domain includes the value.
        It sets the domain to only contain the given value.
        It also removes the value from other cells domains if there's an arc between this cell and the other one.
        :param value: the value to set.
        """
        if value not in get_valid_value_list():
            raise InvalidCellValue(value)

        if value not in self.domain:
            raise ValueNotInDomain(self, value)

        if self.value is not None:
            raise CellOccupied(self, value)

        self.value = value
        self.domain = [value]
        for cell in self.arcs:
            cell.remove_from_domain(value)

    def remove_from_domain(self, value):
        """
        Remove a value from the domain.
        :param value: the value to remove.
        """
        if value in self.domain:
            self.domain.remove(value)

    def auto_fill(self):
        """
        Fill automatically the cell if the domain contains only one value.
        """
        if self.value is None and len(self.domain) == 1:
            self.set_value(self.domain[0])
            return True
        else:
            return False

    def set_arcs(self, cells):
        """
        Set the arcs variable to the given list.
        :param cells: the list of cells that are in constraints alongside with this cell.
        """
        self.arcs = cells

    def get_unassigned_variables_constraints(self):
        """
        Unassigned variables constraints.
        :return: the amount of constraints in which this cell and an unassigned cell are involved.
        """
        return sum(1 for c in self.arcs if c.value is None)

    def lcv(self):
        """
        Least constraining values
        :return: the ordered possible values based from the least constraining to the most constraining.
        """
        counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        for i in self.domain:
            c = 0
            for cell in self.arcs:
                if i in cell.domain:
                    c += 1
            counts[i] = c

        output = []
        for val in sorted(counts.items(), key=lambda kv: kv[1]):
            if val[1] > 0:
                output.append(val[0])

        return output
