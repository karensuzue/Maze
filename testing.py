import time
from grid import Grid
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive
from image_export.to_png import ToPNG

class TestMethods():
    # Grid size is 30 rows by 20 columns, each algorithm is simulated 50 times
    def __init__(self, grid):
        self.grid = grid

    # Average maze attributes
    def average_straightaways(self):
        """
        Obtain average number of straightaway cells.
        :return: average number of straightaway cells
        """
        straightaways = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            straightaways += g.get_straightaways()

        return straightaways / 50

    def average_turns(self):
        """
        Obtain average number of turn cells.
        :return: average number of turn cells
        """
        turns = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            turns += g.get_turns()

        return turns / 50

    def average_crossroads(self):
        """
        Obtain average number of crossroad cells.
        :return: average number of crossroad cells
        """
        crossroads = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            crossroads += g.get_crossroads()

        return crossroads / 50

    def average_tjunctions(self):
        """
        Obtain average number of T-junction cells.
        :return: average number of T-junction cells
        """
        tjunctions = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            tjunctions += g.get_tjunctions()

        return tjunctions / 50

    def average_terminals(self):
        """
        Obtain average number of terminal cells.
        :return: average number of terminal cells
        """
        terminals = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            terminals += g.get_terminals()

        return terminals / 50

    # Average solution attributes
    def avg_solution_straightaways(self):
        """
        Obtain average number of straightaway cells for solution path.
        :return: average number of straightaway cells for solution path
        """
        straightaways = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            straightaways += self.get_straightaways_solution(path, g)

        return straightaways / 50

    def avg_solution_turns(self):
        """
        Obtain average number of turn cells for solution path.
        :return: average number of turn cells for solution path
        """
        turns = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            turns += self.get_turns_solution(path, g)

        return turns / 50

    def avg_solution_crossroads(self):
        """
        Obtain average number of crossroad cells for solution path.
        :return: average number of crossroad cells for solution path
        """
        crossroads = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            crossroads += self.get_crossroads_solution(path, g)

        return crossroads / 50

    def avg_solution_tjunctions(self):
        """
        Obtain average number of T-junction cells for solution path.
        :return: average number of T-junction cells for solution path
        """
        tjunctions = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            tjunctions += self.get_tjunctions_solution(path, g)

        return tjunctions / 50

    def avg_solution_terminals(self):
        """
        Obtain average number of terminal cells for solution path.
        :return: average number of terminal cells for solution path
        """
        terminals = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            terminals += self.get_terminals_solution(path, g)

        return terminals / 50

    def get_straightaways_solution(self, arr, grid):
        """
        Obtain number of straightaway cells for the solution path.
        :param arr: an array of solution path cells
        :param grid: a Grid object for the maze
        :return: the number of straightaway cells in the solution path
        """
        straightaways = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

            if cell.exist_link(east) and not (
                    cell.exist_link(north) or cell.exist_link(south)):
                if cell.exist_link(west):
                    straightaways += 1

            if cell.exist_link(north) and not (
                    cell.exist_link(east) or cell.exist_link(west)):
                if cell.exist_link(south):
                    straightaways += 1

        return straightaways

    def get_turns_solution(self, arr, grid):
        """
        Obtain number of turn cells for the solution path.
        :param arr: an array of solution path cells
        :param grid: a Grid object for the maze
        :return: the number of turn cells in the solution path
        """
        turns = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

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

    def get_crossroads_solution(self, arr, grid):
        """
        Obtain number of crossroad cells for the solution path.
        :param arr: an array of solution path cells
        :param grid: a Grid object for the maze
        :return: the number of crossroad cells in the solution path
        """
        crossroads = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

            if cell.exist_link(north) and cell.exist_link(
                    south) and cell.exist_link(east) and cell.exist_link(west):
                crossroads += 1

        return crossroads

    def get_tjunctions_solution(self, arr, grid):
        """
        Obtain number of T-junction cells for the solution path.
        :param arr: an array of solution path cells
        :param grid: a Grid object for the maze
        :return: the number of T-junction cells in the solution path
        """
        junctions = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

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

    def get_terminals_solution(self, arr, grid):
        """
        Obtain number of terminal cells for the solution path.
        :param arr: an array of solution path cells
        :param grid: a Grid object for the maze
        :return: the number of terminal cells in the solution path
        """
        terminal = 0
        for i in range(len(arr)):
            cell = arr[i]
            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

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


    # Average timing methods
    def average_binary_time(self):
        """
        Obtain average generation time for the Binary Tree algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_binary()
        return time / 50

    def average_sidewinder_time(self):
        """
        Obtain average generation time for the Sidewinder algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_sidewinder()
        return time / 50

    def average_prim_time(self):
        """
        Obtain average generation time for Prim's algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_prim()
        return time / 50

    def average_kruskal_time(self):
        """
        Obtain average generation time for Kruskal's algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_kruskal()
        return time / 50

    def average_wilson_time(self):
        """
        Obtain average generation time for Wilson's algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_wilson()
        return time / 50

    def average_recursive_time(self):
        """
        Obtain average generation time for Recursive Backtracker algorithm.
        :return: the average generation time
        """
        time = 0
        for i in range(50):
            self.grid = Grid(30, 20)
            time += self.time_recursive()
        return time / 50

    # Individual timing methods
    def time_binary(self):
        """
        Obtain generation time for the Binary Tree algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        BinaryTree().generate(self.grid)
        return time.time() - start_time

    def time_sidewinder(self):
        """
        Obtain generation time for the Sidewinder algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        Sidewinder().generate(self.grid)
        return time.time() - start_time

    def time_prim(self):
        """
        Obtain generation time for Prim's algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        Prim().generate(self.grid)
        return time.time() - start_time

    def time_kruskal(self):
        """
        Obtain generation time for Kruskal's algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        kruskal = Kruskal(self.grid)
        kruskal.generate(self.grid)
        return time.time() - start_time

    def time_wilson(self):
        """
        Obtain generation time for Wilson's algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        Wilson().generate(self.grid)
        return time.time() - start_time

    def time_recursive(self):
        """
        Obtain generation time for Recursive Backtracker algorithm.
        :return: the time it takes to generate a maze
        """
        start_time = time.time()
        Recursive().generate(self.grid)
        return time.time() - start_time

    # Count number of cells in solution path
    def avg_cell_solution(self):
        """
        Count average number of cells in solution path
        :return: the average number of cells in solution path
        """
        cells = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            cells += len(path)

        return cells / 50


if __name__ == '__main__':
    grid = Grid(30, 20)

    test = TestMethods(grid)
    # print("Average Binary Time: ", test.average_binary_time())
    # print("Average Sidewinder Time: ", test.average_sidewinder_time())
    # print("Average Kruskal Time: ", test.average_kruskal_time())
    # print("Average Recursive Time: ", test.average_recursive_time())
    # print("Average Wilson Time: ", test.average_wilson_time())
    print("Average Prim Time: ", test.average_prim_time())

    print("Average Straightaways: ", test.average_straightaways())
    print("Average Turns: ", test.average_turns())
    print("Average Crossroads: ", test.average_crossroads())
    print("Average T-junctions: ", test.average_tjunctions())
    print("Average Terminals: ", test.average_terminals())

    # print("AVERAGE Binary Tree Solution Path Cells: ", test.avg_cell_solution())
    # print("AVERAGE Sidewinder Solution Path Cells: ", test.avg_cell_solution())
    # print("AVERAGE Kruskal Solution Path Cells: ", test.avg_cell_solution())
    # print("AVERAGE Recursive Solution Path Cells: ", test.avg_cell_solution())
    # print("AVERAGE Wilson Solution Path Cells: ", test.avg_cell_solution())
    print("AVERAGE Prim Solution Path Cells: ", test.avg_cell_solution())

    print("Average Solution Straightaways: ", test.avg_solution_straightaways())
    print("Average Solution Turns: ", test.avg_solution_turns())
    print("Average Solution Crossroads: ", test.avg_solution_crossroads())
    print("Average Solution T-junctions: ", test.avg_solution_tjunctions())
    print("Average Solution Terminals: ", test.avg_solution_terminals())

