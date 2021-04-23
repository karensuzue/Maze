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
                           "Recursive Backtracker": 5,
                           "Wilson's": 6}
        self.v_algorithm = IntVar()
        self.v_algorithm.set(1)
        for (text, value) in self.algorithms.items():
            Radiobutton(self.menu, text=text, variable=self.v_algorithm,
                        value=value).pack()

        # Plain maze, colored bias map, or solution highlighted
        self.map_label = Label(self.menu, text="Maze rendering options:")
        self.v_render = IntVar()
        self.v_render.set(1)
        self.plain_option = Radiobutton(self.menu, text="Plain Maze",
                                        variable=self.v_render, value=1)
        self.solution_option = Radiobutton(self.menu,
                                           text="Maze with Solution Path",
                                           variable=self.v_render, value=2)
        self.color_option = Radiobutton(self.menu, text="Colored Maze",
                                        variable=self.v_render, value=3)


        self.map_label.pack()
        self.plain_option.pack()
        self.solution_option.pack()
        self.color_option.pack()

        # Generate button
        self.generate_button = Button(self.menu, text="Generate Maze",
                                      command=self.generate)
        self.generate_button.pack()

        # Maze details button
        self.details_button = Button(self.menu, text="Maze Attributes", command=self.get_attributes)
        self.details_button.pack()

        # Reset button
        self.reset_button = Button(self.menu, text="Reset", command=self.reset)
        self.reset_button.pack()

    def get_attributes(self):
        # New window
        new_window = Toplevel(self.master)
        new_window.title("Maze Attributes")

        Label(new_window, width=40, pady=1).pack()

        label1 = Label(new_window, text="Maze Attributes:", width=40)
        label1.pack()

        size = self.grid.get_size()
        straightaways = self.grid.get_straightaways()
        turns = self.grid.get_turns()
        crossroads = self.grid.get_crossroads()
        tjunctions = self.grid.get_tjunctions()
        terminals = self.grid.get_terminals()

        Label(new_window, text="Total number of cells: " + str(size), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Straightaways: " + str(straightaways), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Turns: " + str(turns), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Crossroads: " + str(crossroads), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="T-junctions: " + str(tjunctions),
              width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Terminals " + str(terminals),
              width=40, anchor="w", padx=10).pack()

        Label(new_window, width=40, pady=1).pack()

        label2 = Label(new_window, text="Solution Path Attributes:")
        label2.pack()
        render = ToPNG(self.grid, CELL_SIZE)
        solution_path = render.render_path()
        straightaways_solution = self.get_straightaways_solution(solution_path)
        turns_solution = self.get_turns_solution(solution_path)
        crossroads_solution = self.get_crossroads_solution(solution_path)
        tjunctions_solution = self.get_tjunctions_solution(solution_path)
        terminals_solution = self.get_terminals_solution(solution_path)

        Label(new_window, text="Number of cells: " + str(len(solution_path)), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Straightaways: " + str(straightaways_solution), width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Turns: " + str(turns_solution),
              width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Crossroads: " + str(crossroads_solution),
              width=40, anchor="w", padx=10).pack()
        Label(new_window, text="T-junctions: " + str(tjunctions_solution),
              width=40, anchor="w", padx=10).pack()
        Label(new_window, text="Terminals: " + str(terminals_solution),
              width=40, anchor="w", padx=10).pack()
        Label(new_window, width=40, pady=1).pack()


    def get_straightaways_solution(self, arr):
        straightaways = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = self.grid.get_north(cell)
            south = self.grid.get_south(cell)
            east = self.grid.get_east(cell)
            west = self.grid.get_west(cell)

            if cell.exist_link(east) and not (
                    cell.exist_link(north) or cell.exist_link(south)):
                if cell.exist_link(west):
                    straightaways += 1

            if cell.exist_link(north) and not (
                    cell.exist_link(east) or cell.exist_link(west)):
                if cell.exist_link(south):
                    straightaways += 1

        return straightaways

    def get_turns_solution(self, arr):
        turns = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = self.grid.get_north(cell)
            south = self.grid.get_south(cell)
            east = self.grid.get_east(cell)
            west = self.grid.get_west(cell)

            if cell.exist_link(north) and not cell.exist_link(south):
                if cell.exist_link(east) and not cell.exist_link(west):
                    turns += 1

                if cell.exist_link(west) and not cell.exist_link(east):
                    turns += 1

            if cell.exist_link(south) and not cell.exist_link(north):
                if cell.exist_link(east) and not cell.exist_link(west):
                    turns += 1

                if cell.exist_link(west) and not cell.exist_link(east):
                    turns += 1

        return turns

    def get_crossroads_solution(self, arr):
        crossroads = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = self.grid.get_north(cell)
            south = self.grid.get_south(cell)
            east = self.grid.get_east(cell)
            west = self.grid.get_west(cell)

            if cell.exist_link(north) and cell.exist_link(
                    south) and cell.exist_link(east) and cell.exist_link(west):
                crossroads += 1

        return crossroads

    def get_tjunctions_solution(self, arr):
        junctions = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = self.grid.get_north(cell)
            south = self.grid.get_south(cell)
            east = self.grid.get_east(cell)
            west = self.grid.get_west(cell)

            if cell.exist_link(north) and cell.exist_link(south):
                if cell.exist_link(west) and not cell.exist_link(east):
                    junctions += 1

                if cell.exist_link(east) and not cell.exist_link(west):
                    junctions += 1

            if cell.exist_link(west) and cell.exist_link(east):
                if cell.exist_link(north) and not cell.exist_link(south):
                    junctions += 1

                if cell.exist_link(south) and not cell.exist_link(north):
                    junctions += 1

        return junctions

    def get_terminals_solution(self, arr):
        terminal = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = self.grid.get_north(cell)
            south = self.grid.get_south(cell)
            east = self.grid.get_east(cell)
            west = self.grid.get_west(cell)

            if cell.exist_link(north) and not (
                    cell.exist_link(south) or cell.exist_link(
                    east) or cell.exist_link(west)):
                terminal += 1

            if cell.exist_link(south) and not (
                    cell.exist_link(north) or cell.exist_link(
                    east) or cell.exist_link(west)):
                terminal += 1

            if cell.exist_link(east) and not (
                    cell.exist_link(north) or cell.exist_link(
                    south) or cell.exist_link(west)):
                terminal += 1

            if cell.exist_link(west) and not (
                    cell.exist_link(north) or cell.exist_link(
                    south) or cell.exist_link(east)):
                terminal += 1

        return terminal

    def image_load(self):
        if self.v_render.get() == 1:
            image = Image.open("maze.png")
            return ImageTk.PhotoImage(image)

        if self.v_render.get() == 2:
            image = Image.open("maze-solution.png")
            return ImageTk.PhotoImage(image)

        if self.v_render.get() == 3:
            image = Image.open("maze-colored.png")
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

        # if self.v_algorithm.get() == 4:
            # Prim().generate(self.grid)

        if self.v_algorithm.get() == 5:
            Recursive().generate(self.grid)

        if self.v_algorithm.get() == 6:
            Wilson().generate(self.grid)

        # Render choice
        render = ToPNG(self.grid, CELL_SIZE)

        if self.v_render.get() == 1:
            render.render()

        if self.v_render.get() == 2:
            render.render_path()

        if self.v_render.get() == 3:
            render.render_color()

        # New window to display generated maze
        new_window = Toplevel(self.master)
        new_window.title("Display Maze")

        # Maze image
        img = self.image_load()
        img_label = Label(new_window, image=img)
        img_label.image = img
        img_label.pack()


if __name__ == '__main__':
    root = Tk()
    # root.geometry("700x500")
    my_gui = GUI(root)
    root.mainloop()
