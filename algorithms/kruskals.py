import random
from grid import Grid
from grid import Cell


class Subset():
    # Wrap cells in Subset class, gives them ability to track subset IDs
    def __init__(self, cell, id):
        self.cells = [cell]
        self.size = 1
        self.id = id  # Subset ID changes when they're merged

class Kruskal():
    def __init__(self, grid):
        # A set is created for each cell
        self.edges = grid.get_edges()
        self.find_subset = {}
        self.find_cells = {}  # Maps cells to their subset IDs

        # Assign subset ID to each cell
        counter = 0
        for r in range(grid.rows):
            for c in range(grid.cols):
                cell = grid.grid[r][c]
                # Subset's unique ID is counter
                subset = Subset(cell, counter)

                self.find_subset[cell] = subset
                self.find_cells[subset] = subset.cells # or cell
                counter += 1

    def can_merge(self, left, right):
        if self.find_subset[left] != self.find_subset[right]:
            return True
        return False

    def merge(self, left, right):
        left.link(right)
        right.link(left)

        winner = self.find_subset[left]
        loser = self.find_subset[right]

        for cell in loser.cells:
            winner.cells.append(cell)
            self.find_cells[winner].append(cell)
            self.find_subset[cell] = winner

        self.find_cells.pop(loser)

    def generate(self, grid):
        while len(self.edges) > 0:
            random_edge = random.choice(self.edges)
            self.edges.remove(random_edge)

            cell_1 = random_edge[0]
            cell_2 = random_edge[1]

            if self.can_merge(cell_1, cell_2):
                self.merge(cell_1, cell_2)