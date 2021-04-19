import time
from grid import Grid
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive

class TestMethods():
    # Grid size is 30 rows by 20 columns, each algorithm is simulated 50 times
    def __init__(self, grid):
        self.grid = grid

    # Average maze attributes
    def average_straightaways(self):
        straightaways = 0
        for i in range(50):
            g = Grid(30, 20)

            BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            straightaways += g.get_straightaways()

        return straightaways // 50

    def average_turns(self):
        turns = 0
        for i in range(50):
            g = Grid(30, 20)

            BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            turns += g.get_turns()

        return turns // 50

    def average_crossroads(self):
        crossroads = 0
        for i in range(50):
            g = Grid(30, 20)

            BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            crossroads += g.get_crossroads()

        return crossroads // 50

    def average_tjunctions(self):
        tjunctions = 0
        for i in range(50):
            g = Grid(30, 20)

            BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            tjunctions += g.get_tjunctions()

        return tjunctions // 50

    def average_terminals(self):
        terminals = 0
        for i in range(50):
            g = Grid(30, 20)

            BinaryTree().generate(g)

            # Sidewinder().generate(g)

            # Prim().generate(g)

            # kruskal = Kruskal(g)
            # kruskal.generate(g)

            # Wilson().generate(g)

            # Recursive().generate(g)

            terminals += g.get_terminals()

        return terminals // 50

    # Average solution attributes
    def avg_solution_straightaways(self):
        pass

    def avg_solution_turns(self):
        pass

    def avg_solution_crossroads(self):
        pass

    def avg_solution_tjunctions(self):
        pass

    def avg_solution_terminals(self):
        pass

    # Average timing methods
    def average_binary_time(self):
        time = 0
        for i in range(50):
            time += self.time_binary()
        return time // 50

    def average_sidewinder_time(self):
        time = 0
        for i in range(50):
            time += self.time_sidewinder()
        return time // 50

    def average_prim_time(self):
        time = 0
        for i in range(50):
            time += self.time_prim()
        return time // 50

    def average_kruskal_time(self):
        time = 0
        for i in range(50):
            time += self.time_kruskal()
        return time // 50

    def average_wilson_time(self):
        time = 0
        for i in range(50):
            time += self.time_wilson()
        return time // 50

    def average_recursive_time(self):
        time = 0
        for i in range(50):
            time += self.time_recursive()
        return time // 50

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
    print("Average Binary Time", test.average_binary_time())
    print("Average Sidewinder Time", test.average_sidewinder_time())
    print("Average Straightaways", test.average_straightaways())