from grid import *

g = Grid()
for c in g.cells:
    c.setValue(c.yPos)
print(g)
