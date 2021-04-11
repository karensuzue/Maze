from grid import Grid
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive


def main():
    # straightaways = 0
    # for i in range(100):
    #    grid = Grid(20, 20)
    #    BinaryTree().generate(grid)
    #    straightaways += grid.get_straightaways()

    # print("Average straightaways ", straightaways//100)

    grid = Grid(20, 20)

    # BinaryTree().generate(grid)
    # print("Binary Tree Algorithm:")

    # Sidewinder().generate(grid)
    # print("Sidewinder Algorithm: ")

    # Prim().generate(grid)
    # print("Prim's Algorithm: ")

    # Wilson().generate(grid)
    # print("Wilson's Algorithm: ")

    # kruskal = Kruskal(grid)
    # kruskal.generate(grid)
    # print("Kruskal's Algorithm: ")

    Recursive().generate(grid)
    print("Recursive Backtracker Algorithm: ")

    grid.print_grid()
    print("Total amount of cells", grid.get_size())
    print("Straightaways", grid.get_straightaways())
    print("Turns", grid.get_turns())
    print("Crossroads", grid.get_crossroads())
    print("T-junctions", grid.get_tjunctions())
    print("Terminals", grid.get_terminals())


if __name__ == '__main__':
    main()
