import random
from grid import Grid
from grid import Cell

class Prim():
    def generate(self, grid):
        first = grid.random_cell()
        active = [first]

        while len(active) > 0:
            random_index = random.randint(0, len(active) - 1)
            cell = active[random_index]

            north = grid.get_north(cell)
            south = grid.get_south(cell)
            east = grid.get_east(cell)
            west = grid.get_west(cell)

            available_neighbors = []

            if not cell.exist_link(north) and north is not None:
                available_neighbors.append(north)

            if not cell.exist_link(south) and south is not None:
                available_neighbors.append(south)

            if not cell.exist_link(east) and east is not None:
                available_neighbors.append(east)

            if not cell.exist_link(west) and west is not None:
                available_neighbors.append(west)

            if len(available_neighbors) > 0:
                random_index = random.randint(0, len(available_neighbors) - 1)
                neighbor = available_neighbors[random_index]
                cell.link(neighbor)
                active.append(neighbor)

            else:
                active.remove(cell)

            #print(active)

