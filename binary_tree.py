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
                if g[r][c].north is not None:
                    neighbors.append(g[r][c].north)
                if g[r][c].east is not None:
                    neighbors.append(g[r][c].east)

                index = random.randint(0, len(neighbors) - 1)
                neighbor = neighbors[index]
                cell = g[neighbor[0]][neighbor[1]]
                g[r][c].link(cell)

        return grid