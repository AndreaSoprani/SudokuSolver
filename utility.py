def get_valid_value_list():
    """
    Used to get a list of the valid values both for cell value and for positions.
    :return: a list with values from 1 to 9
    """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def string_to_int_list(input_string):

    output = []

    for c in input_string:
        output.append(int(c))

    return output


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
        output += get_valid_value_list()
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
        output += get_valid_value_list()
        output += "."
        return output


class ValueNotInDomain(Exception):
    """
    Exception to be called if a cell is being filled with a value which is not in the domain
    """
    cell = None
    value = None

    def __init__(self, cell, value):
        self.cell = cell
        self.value = value

    def __str__(self):
        output = "New value not in domain.\n"
        output += "Cell position: (" + str(self.cell.xPos) + ", " + str(self.cell.yPos) + ").\n"
        output += "Domain: " + str(self.cell.domain) + "."
        output += "New value: " + str(self.value) + "."
        return output


class CellOccupied(Exception):
    """
    Exception to be called if a filled cell is being filled again
    """
    cell = None
    value = None

    def __init__(self, cell, value):
        self.cell = cell
        self.value = value

    def __str__(self):
        output = "Cell already occupied.\n"
        output += "Cell position: (" + str(self.cell.xPos) + ", " + str(self.cell.yPos) + ").\n"
        output += "Old value: " + str(self.cell.value) + "."
        output += "New value: " + str(self.value) + "."
        return output


class VariableSelectionModeUnsupported(Exception):
    """
    Exception called when the variable selection mode is unsupported
    """
    requestedMode = None

    def __init__(self, mode):
        self.requestedMode = mode

    def __str__(self):
        return self.requestedMode + " is not a supported variable selection mode"
