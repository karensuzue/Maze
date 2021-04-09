import random
from grid import Grid
from grid import Cell


class Wilson():
    def generate(self, grid):
        unvisited = []
        for r in range(grid.rows):
            for c in range(grid.cols):
                unvisited.append(grid.grid[r][c])

        random_index = random.randint(0, len(unvisited) - 1)
        first = unvisited[random_index]
        unvisited.remove(first)

        while len(unvisited) > 0:
            random_index = random.randint(0, len(unvisited) - 1)
            cell = unvisited[random_index]
            path = [cell]

            while cell in unvisited:
                neighbors = grid.get_neighbors(cell)
                random_index = random.randint(0, len(neighbors) - 1)
                cell = neighbors[random_index]

                if cell in path:
                    cell_index = path.index(cell)
                    path = path[: cell_index + 1]

                else:
                    path.append(cell)

            for i in range(len(path) - 1):
                path[i].link(path[i + 1])
                unvisited.remove(path[i])
