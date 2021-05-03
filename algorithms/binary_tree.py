import random
from grid import Grid
from grid import Cell


class BinaryTree():
    # Binary tree algorithm with Northeast bias. Starts from Southwest corner.
    def generate(self, grid):
        """
        Generate a maze given a grid of cells.
        :param grid: a Grid object
        :return: a generated maze
        """
        g = grid.grid
        for r in range(grid.rows - 1, -1, -1):
            for c in range(grid.cols):
                neighbors = []
                north_cell = grid.get_north(g[r][c])
                east_cell = grid.get_east(g[r][c])

                if north_cell:
                    neighbors.append(north_cell)
                if east_cell:
                    neighbors.append(east_cell)

                if len(neighbors) > 0:
                    index = random.randint(0, len(neighbors) - 1)
                    neighbor = neighbors[index]
                    if neighbor:
                        g[r][c].link(neighbor)

                    neighbors.clear()

