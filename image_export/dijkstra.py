import random
from grid import Grid
from grid import Cell


class Distance():
    def __init__(self, root):
        self.root = root
        self.cells = {}  # Stores distances of each cell
        self.cells[root] = 1


class Dijkstra():
    def __init__(self):
        self.distances = None

    def solve(self, grid, row, col):
        """
        Solve a maze.
        :param grid: a Grid object representing the maze
        :param row: the row index of the starting cell
        :param col: the column index of the starting cell
        :return: each cell in maze is given a distance value
        """
        start = grid.grid[row][col]
        start.distance = 1
        self.distances = Distance(start)
        frontier = [start]

        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked in cell.links:
                    # Linked cell hasn't been visited
                    if linked not in self.distances.cells:
                        # Distance of linked cell from root = distance of
                        # the current cell + 1
                        self.distances.cells[linked] = self.distances.cells[cell] + 1
                        linked.distance = cell.distance + 1
                        new_frontier.append(linked)

            frontier = new_frontier

    def color_for_cell(self, cell):
        """
        Obtain RGB decimal code to color cell.
        :param cell: a Cell object from the grid/maze
        :return: an RGB decimal code
        """
        if cell in self.distances.cells:
            distance = self.distances.cells[cell]
            maximum = max(self.distances.cells.values())
            intensity = (maximum - distance) / maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            return (dark, dark, bright)

        else:
            return None
