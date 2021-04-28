import random
from grid import Grid
from grid import Cell

class Prim():
    def grid_to_list(self, grid):
        list = []
        for r in range(grid.rows):
            for c in range(grid.cols):
                list.append(grid.grid[r][c])
        return list

    def generate(self, grid):
        grid_list = self.grid_to_list(grid)
        first = grid.random_cell()
        path = [first]
        grid_list.remove(first)

        frontier = []

        while len(grid_list) > 0:
            cell = random.choice(path)

            neighbors = grid.get_neighbors(cell)
            frontier.extend(neighbors)
            neighbor = random.choice(neighbors)
            if neighbor not in path:
                cell.link(neighbor)
                path.append(neighbor)
                frontier.remove(neighbor)
                grid_list.remove(neighbor)