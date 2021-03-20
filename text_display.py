from grid import Cell
from grid import Grid
from binary_tree import BinaryTree


def main():
    grid = Grid(4, 4)
    temp = grid.grid[0][3]
    print(temp.north)
    print(temp.west)
    print(temp.east)
    print(temp.south)
    random = grid.random_cell()
    print(random)

    grid = BinaryTree().generate(grid)
    grid.print_grid()


if __name__ == '__main__':
    main()
