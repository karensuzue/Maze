import random
from grid import Grid
from grid import Cell


class Subset():
    # Wrap cells in Subset class, gives them ability to track subset IDs
    def __init__(self, cell):
        self.cells = [cell]
        self.size = 1

class Kruskal():
    def __init__(self, grid):
        # A set is created for each cell
        self.edges = grid.get_edges()
        self.find_subset = {}
        self.find_cells = {}  # Maps cells to their subset IDs

        # Assign subset ID to each cell
        for r in range(grid.rows):
            for c in range(grid.cols):
                cell = grid.grid[r][c]
                # Subset's unique ID is counter
                subset = Subset(cell)

                self.find_subset[cell] = subset
                # Instead of making a new array, pointer? to the cells array
                # already initialized in subset, so performance is faster
                # When appending cells (like below) they will be added to
                # this subset's cells array
                self.find_cells[subset] = subset.cells

    def can_merge(self, left, right):
        if self.find_subset[left] != self.find_subset[right]:
            return True
        return False

    def merge(self, left, right):
        left.link(right)
        right.link(left)

        winner = self.find_subset[left]
        loser = self.find_subset[right]

        # Move contents of loser set into winner set
        for cell in loser.cells:
            #winner.cells.append(cell)
            self.find_cells[winner].append(cell)
            self.find_subset[cell] = winner
        # Pop loser set
        self.find_cells.pop(loser)

    def generate(self, grid):
        while len(self.edges) > 0:
            random_edge = random.choice(self.edges)
            self.edges.remove(random_edge)

            cell_1 = random_edge[0]
            cell_2 = random_edge[1]

            if self.can_merge(cell_1, cell_2):
                self.merge(cell_1, cell_2)