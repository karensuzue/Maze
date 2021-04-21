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
        straightaways = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            straightaways += g.get_straightaways()

        return straightaways / 50

    def average_turns(self):
        turns = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            turns += g.get_turns()

        return turns / 50

    def average_crossroads(self):
        crossroads = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            crossroads += g.get_crossroads()

        return crossroads / 50

    def average_tjunctions(self):
        tjunctions = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            tjunctions += g.get_tjunctions()

        return tjunctions / 50

    def average_terminals(self):
        terminals = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            terminals += g.get_terminals()

        return terminals / 50

    # Average solution attributes
    def avg_solution_straightaways(self):
        straightaways = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            straightaways += self.get_straightaways_solution(path, g)

        return straightaways / 50

    def avg_solution_turns(self):
        turns = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            turns += self.get_turns_solution(path, g)

        return turns / 50

    def avg_solution_crossroads(self):
        crossroads = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            crossroads += self.get_crossroads_solution(path, g)

        return crossroads / 50

    def avg_solution_tjunctions(self):
        tjunctions = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            tjunctions += self.get_tjunctions_solution(path, g)

        return tjunctions / 50

    def avg_solution_terminals(self):
        terminals = 0
        for i in range(50):
            g = Grid(30, 20)

            # BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            Wilson().generate(g)

            # Recursive().generate(g)

            render = ToPNG(g, 5)
            path = render.render_path2()
            terminals += self.get_terminals_solution(path, g)

        return terminals / 50

    def get_straightaways_solution(self, arr, grid):
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
        time = 0
        for i in range(50):
            time += self.time_binary()
        return time / 50

    def average_sidewinder_time(self):
        time = 0
        for i in range(50):
            time += self.time_sidewinder()
        return time / 50

    def average_prim_time(self):
        time = 0
        for i in range(50):
            time += self.time_prim()
        return time / 50

    def average_kruskal_time(self):
        time = 0
        for i in range(50):
            time += self.time_kruskal()
        return time / 50

    def average_wilson_time(self):
        time = 0
        for i in range(50):
            time += self.time_wilson()
        return time / 50

    def average_recursive_time(self):
        time = 0
        for i in range(50):
            time += self.time_recursive()
        return time / 50

    # Individual timing methods
    def time_binary(self):
        start_time = time.time()
        BinaryTree().generate(self.grid)
        return time.time() - start_time

    def time_sidewinder(self):
        start_time = time.time()
        Sidewinder().generate(self.grid)
        return time.time() - start_time

    def time_prim(self):
        start_time = time.time()
        Prim().generate(self.grid)
        return time.time() - start_time

    def time_kruskal(self):
        start_time = time.time()
        kruskal = Kruskal(self.grid)
        kruskal.generate(self.grid)
        return time.time() - start_time

    def time_wilson(self):
        start_time = time.time()
        Wilson().generate(self.grid)
        return time.time() - start_time

    def time_recursive(self):
        start_time = time.time()
        Recursive().generate(self.grid)
        return time.time() - start_time


if __name__ == '__main__':
    grid = Grid(30, 20)

    test = TestMethods(grid)
    # print("Average Binary Time: ", test.average_binary_time())
    # print("Average Sidewinder Time: ", test.average_sidewinder_time())
    # print("Average Kruskal Time: ", test.average_kruskal_time())
    # print("Average Recursive Time: ", test.average_recursive_time())
    # print("Average Wilson Time: ", test.average_wilson_time())

    # print("Binary Tree Solution Path")
    # print("Sidewinder Solution Path")
    # print("Kruskal Solution Path")
    # print("Recursive Solution Path")
    print("Wilson Solution Path")

    # print("Average Solution Straightaways: ", test.avg_solution_straightaways())
    # print("Average Solution Turns: ", test.avg_solution_turns())
    print("Average Solution Crossroads: ", test.avg_solution_crossroads())
    print("Average Solution T-junctions: ", test.avg_solution_tjunctions())
    print("Average Solution Terminals: ", test.avg_solution_terminals())
