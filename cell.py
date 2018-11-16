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


    def __init__(self, xPos, yPos):
        """
        Initializes an empty cell in a given position.
        :param xPos: the x position of the cell (from 1 to 9).
        :param yPos: the y position of the cell (from 1 to 9).
        """

        if xPos not in getValidValueList() :
            raise InvalidPosition("xPos", xPos)
        if yPos not in getValidValueList() :
            raise InvalidPosition("yPos", yPos)

        self.xPos = xPos
        self.yPos = yPos
        self.domain = getValidValueList()

    def setValue(self, value):
        """
        Sets the value of the cell to a given value.
        The setting is performed only if the previous value is None and the domain includes the value.
        It also sets the domain to only contain the given value.
        :param value: the value to set.
        """
        if value not in getValidValueList():
            raise InvalidCellValue(value)

        if self.value is None and value in self.domain :
            self.value = value
            self.domain = [value]

    def removeFromDomain(self, value):
        """
        Removes a value from the domain.
        :param value: the value to remove.
        """
        self.domain.remove(value)

    def autoFill(self):
        """
        Fills automatically the cell if the domain contains only one value.
        """
        if self.value is None and len(self.domain) == 1 :
            self.value = self.domain[0]

    def __str__(self):
        """
        String representation of the cell.
        :return: the value as a string. If the value is None returns a whitespace.
        """
        if self.value is None:
            return " "
        return str(self.value)

