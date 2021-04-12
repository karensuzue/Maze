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

    def solve(self, grid):
        # Start from the middle of the maze
        start = grid.grid[grid.rows // 2 - 1][grid.cols // 2 - 1]
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
        if cell in self.distances.cells:
            distance = self.distances.cells[cell]
            maximum = max(self.distances.cells.values())
            intensity = (maximum - distance) / maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            return (dark, dark, bright)

        else:
            return None
