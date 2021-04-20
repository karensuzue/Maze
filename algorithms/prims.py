import random
from grid import Grid
from grid import Cell

class Prim():
    def find_neighbors(self, cell, grid):
        # Find available neighbors
        neighbors = []
        north = grid.get_north(cell)
        south = grid.get_south(cell)
        east = grid.get_east(cell)
        west = grid.get_west(cell)

        if not cell.exist_link(north) and north is not None:
            neighbors.append(north)

        if not cell.exist_link(south) and south is not None:
            neighbors.append(south)

        if not cell.exist_link(east) and east is not None:
            neighbors.append(east)

        if not cell.exist_link(west) and west is not None:
            neighbors.append(west)

        return neighbors

    def min_key(self, dic):
        minimum = random.choice(list(dic))
        for item in dic:
            if dic[item] < dic[minimum]:
                minimum = item
        return minimum

    def min_element(self, arr, costs):
        # Return the element with the lowest cost in the array
        minimum = random.choice(arr)
        for i in range(len(arr)):
            if costs[arr[i]] < costs[minimum]:
                minimum = arr[i]
        return minimum

    def generate(self, grid):
        # Arbitrary starting cell
        first = grid.random_cell()
        active = [first]

        # Assign random costs to each cell (not edges)
        costs = {}
        for r in range(grid.rows):
            for c in range(grid.cols):
                cell = grid.grid[r][c]
                costs[cell] = random.randint(1, 100)

        while len(active) > 0:
            cell = self.min_element(active, costs)  # Cell with minimum cost
            print(cell)
            available_neighbors = self.find_neighbors(cell, grid)

            # Avoid duplicates
            for i in range(len(available_neighbors)):
                if available_neighbors[i] not in active:
                    active.append(available_neighbors[i])

            if len(available_neighbors) > 0:
                neighbor = self.min_element(active, costs)
                cell.link(neighbor)
                active.remove(neighbor)
                active.extend(self.find_neighbors(neighbor, grid))


            else:
                active.remove(cell)

            #print(active)

