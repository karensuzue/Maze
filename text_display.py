from grid import Cell
from grid import Grid


def main():
    cell1 = Cell(1, 1)
    cell2 = Cell(1, 2)

    cell1.link(cell2)
    print(cell1.links)
    print(cell2.links)
    print(cell2.exist_link(cell1))

    cell2.unlink(cell1)
    print(cell1.links)
    print(cell2.links)
    print(cell1.exist_link(cell2))

    grid = Grid(4, 4)
    print(grid.grid)
    temp = grid.grid[0][0]
    print(temp.north)
    print(temp.west)
    print(temp.east)
    print(temp.south)
    random = grid.random_cell()
    print(random)


if __name__ == '__main__':
    main()
