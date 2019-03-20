from grid import *
import copy


def dfs(variable_selection_mode):
    """
    Solve the sudoku through a depth-first-search.
    :param variable_selection_mode: "mrv" or "degree"
    :return: True if the sudoku is solved. False for recursion purpose (backup and continue).
    """

    global grid

    grid.auto_fill()

    if len(grid.get_unassigned()) == 0:
        return True

    if variable_selection_mode == "degree":
        cell = grid.degree()
    elif variable_selection_mode == "mrv":
        cell = grid.mrv()
    else:
        raise VariableSelectionModeUnsupported(variable_selection_mode)

    index = grid.cells.index(cell)
    lcv = cell.lcv()
    backup = copy.deepcopy(grid)

    while len(lcv) > 0:
        cell.set_value(lcv.pop(0))

        if grid.dead_end():
            grid = copy.deepcopy(backup)
            cell = grid.cells[index]
        elif dfs(variable_selection_mode) is False:
            grid = copy.deepcopy(backup)
            cell = grid.cells[index]
        else:
            return True

    return False


def solve(values_string):

    global grid

    grid = Grid()
    grid.set_initial_values(string_to_int_list(values_string))

    if dfs("mrv") is False:
        print("Error. Sudoku unsolved")
        print(grid)

    return grid
