from grid import Grid
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive

from image_export.to_png import ToPNG

def main():
    grid = Grid(20, 30)

    # BinaryTree().generate(grid)
    # print("Binary Tree Algorithm:")

    # Sidewinder().generate(grid)
    # print("Sidewinder Algorithm: ")

    Prim().generate(grid)
    print("Prim's Algorithm: ")

    # Wilson().generate(grid)
    # print("Wilson's Algorithm: ")

    # kruskal = Kruskal(grid)
    # kruskal.generate(grid)
    # print("Kruskal's Algorithm: ")

    # Recursive().generate(grid)
    # print("Recursive Backtracker Algorithm: ")

    grid.print_grid()
    print("Total amount of cells", grid.get_size())
    print("Straightaways", grid.get_straightaways())
    print("Turns", grid.get_turns())
    print("Crossroads", grid.get_crossroads())
    print("T-junctions", grid.get_tjunctions())
    print("Terminals", grid.get_terminals())
    # print("Terminal cells", grid.get_terminals()[1])
    # print("Number of terminal cells", len(grid.get_terminals()[1]))



if __name__ == '__main__':
    main()
