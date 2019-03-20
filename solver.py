from grid import *
import copy
import time
import gui


def solve(variable_selection_mode):
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
        elif solve(variable_selection_mode) is False:
            grid = copy.deepcopy(backup)
            cell = grid.cells[index]
        else:
            return True

    return False


easySequence = "041600305" \
               "000007002" \
               "005900000" \
               "700005480" \
               "309008020" \
               "000760009" \
               "004300091" \
               "067500004" \
               "090041200"

difficultSequence = "300090100" \
                    "010034000" \
                    "002060530" \
                    "800200305" \
                    "070050000" \
                    "009008600" \
                    "090005070" \
                    "000600018" \
                    "008700000"

evilSequence = "006003004" \
               "010070050" \
               "700600200" \
               "500800300" \
               "090060080" \
               "007009005" \
               "002004006" \
               "070020010" \
               "600300800"

allZeros = "000000000" \
           "000000000" \
           "000000000" \
           "000000000" \
           "000000000" \
           "000000000" \
           "000000000" \
           "000000000" \
           "000000000"


values = string_to_int_list(difficultSequence)

grid = Grid()
grid.set_initial_values(values)

initial_grid = copy.deepcopy(grid)

start_time = time.time()

solve("mrv")

print("--- Execution time: %s seconds ---" % (time.time() - start_time))

gui.show_sudokus(initial_grid, grid)