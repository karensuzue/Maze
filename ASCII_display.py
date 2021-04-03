from grid import Cell
from grid import Grid
from binary_tree import BinaryTree
from sidewinder import Sidewinder


def main():
    # straightaways = 0
    # for i in range(100):
    #    grid = Grid(20, 20)
    #    BinaryTree().generate(grid)
    #    straightaways += grid.get_straightaways()

    # print("Average straightaways ", straightaways//100)

    grid = Grid(5, 5)
    # BinaryTree().generate(grid)
    # print("Binary Tree Algorithm:")
    Sidewinder().generate(grid)
    print("Sidewinder Algorithm: ")
    grid.print_grid()
    print("Total amount of cells", grid.get_size())
    print("Straightaways", grid.get_straightaways())
    print("Turns", grid.get_turns())
    print("Crossroads", grid.get_crossroads())
    print("T-junctions", grid.get_tjunctions())
    print("Terminals", grid.get_terminals())


if __name__ == '__main__':
    main()
