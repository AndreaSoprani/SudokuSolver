def getValidValueList():
    """
    Used to get a list of the valid values both for cell value and for positions.
    :return: a list with values from 1 to 9
    """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


class InvalidPosition(Exception):
    """
    Exception to be called if the x or y position of the cell is invalid.
    """
    coordinate = ""
    value = None

    def __init__(self, coordinate, value):
        self.coordinate = coordinate
        self.value = value

    def __str__(self):
        output = "Invalid cell position for coordinate "
        output += self.coordinate
        output += ".\n"
        output += str(self.value)
        output += " is not a valid position.\n"
        output += "Insert a value from "
        output += getValidValueList()
        output += "."
        return output
class InvalidCellValue(Exception):
    """
    Exception to be called if the value of the cell is invalid.
    """
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        output = "Invalid cell value.\n"
        output += str(self.value)
        output += " is not a valid value.\n"
        output += "Insert a value from "
        output += getValidValueList()
        output += "."
        return output