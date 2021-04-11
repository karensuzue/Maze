import random
from grid import Grid
from grid import Cell

class Recursive():
    def generate(self, grid):
        stack = []
        start = grid.random_cell()
        stack.append(start)

        while len(stack) > 0:
            current = stack[len(stack) - 1]
            neighbors = grid.get_neighbors(current)

            for n in neighbors:
                if current.exist_link(n):
                    neighbors.remove(n)

            if len(neighbors) == 0:
                stack.remove(current)

            else:
                neighbor = random.choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)