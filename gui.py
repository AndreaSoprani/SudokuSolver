from tkinter import *


def show_sudokus(grid1, grid2):

    root = Tk()
    root.title("Sudoku solver")

    canvas_width = 840
    canvas_height = 440

    canvas = Canvas(root,
                    width=canvas_width,
                    height=canvas_height)
    canvas.pack()

    box1 = [canvas_width/21, canvas_height/11, 10*canvas_width/21, 10*canvas_height/11]
    box2 = [11*canvas_width/21, canvas_height/11, 20*canvas_width/21, 10*canvas_height/11]
    canvas.create_rectangle(box1[0], box1[1], box1[2], box1[3])
    canvas.create_rectangle(box2[0], box2[1], box2[2], box2[3])

    show_grid(canvas, box1, grid1)
    show_grid(canvas, box2, grid2)

    root.mainloop()


def show_grid(canvas, box, grid):

    width = box[2] - box[0]
    height = box[3] - box[1]

    for j in range(0, 3):
        for i in range(0, 3):
            if (i + j) % 2 != 0:
                canvas.create_rectangle(box[0] + i * width / 3,
                                        box[1] + j * height / 3,
                                        box[0] + (i + 1) * width / 3,
                                        box[1] + (j + 1) * height / 3,
                                        fill="#aaaaaa")

    cells = []

    for j in range(0, 9):
        for i in range(9):
            cell = [box[0] + i * width / 9,
                    box[1] + j * height / 9,
                    box[0] + (i + 1) * width / 9,
                    box[1] + (j + 1) * height / 9]
            cells.append(cell)
            canvas.create_rectangle(cell[0], cell[1], cell[2], cell[3])

    for i in range(0, len(grid.cells)):
        if grid.cells[i].value is not None:
            canvas.create_text((cells[i][0]+cells[i][2])/2, (cells[i][1]+cells[i][3])/2, text=str(grid.cells[i].value))
