from tkinter import *
from PIL import Image, ImageTk

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

CELL_SIZE = 20

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Maze Generator")

        # Header
        self.header = Label(self.master, text="Maze Generator", padx= 10, pady=5, font=10)
        self.header.pack()

        # Instruction
        self.instruction = Label(self.master, text="Before generating a new maze, click RESET", fg="#f00", padx= 5)
        self.instruction.pack()

        # Menu frame
        self.menu = Frame(self.master)
        self.menu.pack()

        # Initialize grid
        self.grid = Grid(GRID_ROW, GRID_COL)

        # Options for maze generation algorithms
        self.algo_label = Label(self.menu, text="Maze generation algorithms:")
        self.algo_label.pack()
        self.algorithms = {"Binary Tree": 1,
                           "Sidewinder": 2,
                           "Kruskal's": 3,
                           "Prim's": 4,
                           "Recursive Backtracker": 5,
                           "Wilson's": 6}
        self.v_algorithm = IntVar()
        self.v_algorithm.set(1)
        for (text, value) in self.algorithms.items():
            Radiobutton(self.menu, text=text, variable=self.v_algorithm,
                        value=value).pack()

        # Plain maze or colored bias map
        self.map_label = Label(self.menu, text="Maze rendering options:")
        self.v_render = IntVar()
        self.v_render.set(1)
        self.plain_option = Radiobutton(self.menu, text="Plain Maze",
                                        variable=self.v_render, value=1)
        self.color_option = Radiobutton(self.menu, text="Colored Maze",
                                        variable=self.v_render, value=2)

        self.map_label.pack()
        self.plain_option.pack()
        self.color_option.pack()

        # Generate button
        self.generate_button = Button(self.menu, text="Generate Maze",
                                      command=self.generate)
        self.generate_button.pack()

        # Reset button
        self.reset_button = Button(self.menu, text="Reset", command=self.reset)
        self.reset_button.pack()

    def image_load(self):
        if self.v_render.get() == 2:
            image = Image.open("maze-colored.png")
            return ImageTk.PhotoImage(image)
        else:
            image = Image.open("maze.png")
            return ImageTk.PhotoImage(image)

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
        render = ToPNG(self.grid, CELL_SIZE)

        if self.v_render.get() == 1:
            render.render()

        if self.v_render.get() == 2:
            render.render_color()

        # New window to display generated maze
        new_window = Toplevel(self.master)
        new_window.title("Display Maze")

        # Maze image
        img = self.image_load()
        img_label = Label(new_window, image=img)
        img_label.image = img
        img_label.place(x=10, y=10)
        img_label.pack()


if __name__ == '__main__':
    root = Tk()
    # root.geometry("700x500")
    my_gui = GUI(root)
    root.mainloop()
