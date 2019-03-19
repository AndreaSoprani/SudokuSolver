from grid import *
import copy
import sys
sys.setrecursionlimit(10000)

grid = Grid()

def backtracking(variable_selection_mode, counter):

    counter += 1

    global grid

    if len(grid.getUnassigned()) == 0:
        print(grid)
        return True

    cell = None

    if variable_selection_mode == "degree":
        cell = grid.Degree()
    elif variable_selection_mode == "mrv":
        cell = grid.MRV()
    else:
        raise VariableSelectionModeUnsupported(variable_selection_mode)

    index = grid.cells.index(cell)
    lcv = cell.LCV()
    backup = copy.deepcopy(grid)

    while len(lcv) > 0:
        #print("x: " + str(cell.xPos) + ", y: " + str(cell.yPos) + ", lcv: " + str(lcv))
        #print(cell.value)
        cell.SetValue(lcv.pop(0))
        grid.AutoFill()

        if grid.DeadEnd():
            # print("deadend " + str(counter))
            grid = copy.deepcopy(backup)
            cell = grid.cells[index]
            continue
        elif backtracking(variable_selection_mode, counter) is False:
            print("backtrack false " + str(counter))
            print(hex(id(grid)))
            grid = copy.deepcopy(backup)
            print(hex(id(grid)))
            cell = grid.cells[index]
        else:
            if len(grid.getUnassigned()) > 0:
                print("something went wrong")
            print(hex(id(grid)))
            print(counter)
            print(grid)
            return True

    print("false")
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

# values = stringToIntList(easySequence)
values = stringToIntList(difficultSequence)

grid.SetInitialValues(values)
print(grid)

grid.AutoFill()
backtracking("mrv", 0)
print(hex(id(grid)))
print(grid)

for cell in grid.getUnassigned():
    print("xPos: " + str(cell.xPos) + ", yPos: " + str(cell.yPos))

