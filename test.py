from grid import *
import copy
import sys
sys.setrecursionlimit(10000)

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

values = stringToIntList(easySequence)
#values = stringToIntList(difficultSequence)

g = Grid()
g.SetInitialValues(values)


