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

    def __init__(self, xPos, yPos):
        """
        Initializes an empty cell in a given position.
        :param xPos: the x position of the cell (from 1 to 9).
        :param yPos: the y position of the cell (from 1 to 9).
        """

        if xPos not in getValidValueList():
            raise InvalidPosition("xPos", xPos)
        if yPos not in getValidValueList():
            raise InvalidPosition("yPos", yPos)

        self.xPos = xPos
        self.yPos = yPos
        self.domain = getValidValueList()
        self.arcs = []

    def __str__(self):
        """
        String representation of the cell.
        :return: the value as a string. If the value is None returns a whitespace.
        """
        if self.value is None:
            return " "
        return str(self.value)

    def SetValue(self, value):
        """
        Sets the value of the cell to a given value.
        The setting is performed only if the previous value is None and the domain includes the value.
        It sets the domain to only contain the given value.
        It also removes the value from other cells domains if there's an arc between this cell and the other one.
        :param value: the value to set.
        """
        if value not in getValidValueList():
            raise InvalidCellValue(value)

        if value not in self.domain:
            raise ValueNotInDomain(self, value)

        if self.value is not None:
            raise CellOccupied(self, value)

        self.value = value
        #print("x: " + str(self.xPos) + ", y: " + str(self.yPos) + ", val = " + str(value))
        self.domain = [value]
        for cell in self.arcs:
            cell.RemoveFromDomain(value)

    def RemoveFromDomain(self, value):
        """
        Removes a value from the domain.
        :param value: the value to remove.
        """
        if value in self.domain:
            self.domain.remove(value)

    def AutoFill(self):
        """
        Fills automatically the cell if the domain contains only one value.
        """
        if self.value is None and len(self.domain) == 1:
            self.SetValue(self.domain[0])
            return True
        else:
            return False

    def SetArcs(self, cells):
        """
        Sets the arcs variable to the given list.
        :param cells: the list of cells that are in constraints alongside with this cell.
        """
        self.arcs = cells

    def GetUnassignedVariablesConstraints(self):
        """
        Unassigned variables constraints.
        :return: the amount of constraints in which this cell and an unassigned cell are involved.
        """
        return sum(1 for c in self.arcs if c.value is None)

    def LCV(self):
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
