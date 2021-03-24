import random
from grid import Grid
from grid import Cell


class BinaryTree:
    # Binary tree algorithm with Northeast bias. Starts from Southwest corner.
    def generate(self, grid):
        g = grid.grid
        for r in range(grid.rows - 1, 0, -1):
            for c in range(grid.cols):
                neighbors = []
                print("North: ")
                print(g[r][c].north)
                print(g[r][c].south)
                print(g[r][c].east)
                print(g[r][c].west)
                if g[r][c].north is not None:
                    neighbors.append(g[r][c].north)
                if g[r][c].east is not None:
                    neighbors.append(g[r][c].east)

                print(neighbors)

                if len(neighbors) > 0:
                    index = random.randint(0, len(neighbors) - 1)
                    neighbor = neighbors[index]
                    cell = g[neighbor[0]][neighbor[1]]
                    g[r][c].link(cell)
                    print(g[r][c].links)

        return grid
