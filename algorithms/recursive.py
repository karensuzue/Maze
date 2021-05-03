import random
from grid import Grid
from grid import Cell


class Recursive():
    def generate(self, grid):
        """
        Generate a maze given a grid of cells.
        :param grid: a Grid object
        :return: a generated maze
        """
        stack = []
        # Start at Southwest corner
        start = grid.random_cell()
        stack.append(start)

        while len(stack) > 0:
            current = stack[-1]

            neighbors = [n for n in grid.get_neighbors(current) if
                         n.visited is False]

            if len(neighbors) == 0:
                stack.remove(current)

            else:
                random_neighbor = random.choice(neighbors)
                current.link(random_neighbor)
                stack.append(random_neighbor)
                random_neighbor.visited = True
                current.visited = True
