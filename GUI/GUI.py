from tkinter import *
from PIL import Image
from PIL import ImageDraw

from grid import Grid
from image_export.to_png import ToPNG
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive

HEIGHT = 500
WIDTH = 700

GRID_ROW = 30
GRID_COL = 20

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Maze Generator")

        # Initialize grid
        self.grid = Grid(GRID_ROW, GRID_COL)

        # Options for maze generation algorithms
        self.algorithms = {"Binary Tree": 1,
                           "Sidewinder": 2,
                           "Kruskal's": 3,
                           "Prim's": 4,
                           "Recursive Backtracker": 5,
                           "Wilson's": 6}
        self.v_algorithm = IntVar()
        self.v_algorithm.set(1)
        for (text, value) in self.algorithms.items():
            Radiobutton(master, text=text, variable=self.v_algorithm,
                        value=value).pack()

        # Plain maze or colored bias map
        self.map_label = Label(master, text="Maze rendering options:")
        self.v_render = IntVar()
        self.v_render.set(1)
        self.plain_option = Radiobutton(master, text="Plain Maze",
                                        variable=self.v_render, value=1)
        self.color_option = Radiobutton(master, text="Colored Maze",
                                        variable=self.v_render, value=2)

        self.map_label.pack()
        self.plain_option.pack()
        self.color_option.pack()

        # Generate button
        self.generate_button = Button(master, text="Generate Maze",
                                      command=self.generate)
        self.generate_button.pack()

        # Reset button
        self.reset_button = Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def reset(self):
        self.grid = Grid(GRID_ROW, GRID_COL)

    def generate(self):
        # Algorithm choice
        if self.v_algorithm.get() == 1:
            BinaryTree().generate(self.grid)

        if self.v_algorithm.get() == 2:
            Sidewinder().generate(self.grid)

        if self.v_algorithm.get() == 3:
            kruskal = Kruskal(self.grid)
            kruskal.generate(self.grid)

        if self.v_algorithm.get() == 4:
            Prim().generate(self.grid)

        if self.v_algorithm.get() == 5:
            Recursive().generate(self.grid)

        if self.v_algorithm.get() == 6:
            Wilson().generate(self.grid)

        print(self.v_algorithm.get())
        print(self.v_render.get())

        # Render choice
        print(self.grid)
        render = ToPNG(self.grid, 20)

        if self.v_render.get() == 1:
            render.render()

        if self.v_render.get() == 2:
            render.render_color()


if __name__ == '__main__':
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()
