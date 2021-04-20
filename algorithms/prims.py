import random
from grid import Grid
from grid import Cell

class Prim():
    def find_visited_neighbors(self, cell, grid):
        neighbors = []
        north = grid.get_north(cell)
        south = grid.get_south(cell)
        east = grid.get_east(cell)
        west = grid.get_west(cell)

        if north is not None:
            if north.visited:
                neighbors.append(north)

        if south is not None:
            if south.visited:
                neighbors.append(south)

        if east is not None:
            if east.visited:
                neighbors.append(east)

        if west is not None:
            if west.visited:
                neighbors.append(west)

        return neighbors

    def find_unvisited_neighbors(self, cell, grid):
        # Find available neighbors
        neighbors = []
        north = grid.get_north(cell)
        south = grid.get_south(cell)
        east = grid.get_east(cell)
        west = grid.get_west(cell)

        if north is not None:
            if not north.visited:
                neighbors.append(north)

        if south is not None:
            if not south.visited:
                neighbors.append(south)

        if east is not None:
            if not east.visited:
                neighbors.append(east)

        if west is not None:
            if not west.visited:
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
        first = grid.random_cell()
        path = [first]
        while len(path) > 0:
            cell = random.choice(path)
            cell.visited = True

            visited_neighbors = self.find_visited_neighbors(cell, grid)
            unvisited_neighbors = self.find_unvisited_neighbors(cell, grid)

            if len(visited_neighbors) > 0:
                neighbor = random.choice(visited_neighbors)
                cell.link(neighbor)
                path.remove(cell)

            path.extend(unvisited_neighbors)


    def generate2(self, grid):
        first = grid.random_cell()
        walls = [first]
        while len(walls) > 0:
            cell = random.choice(walls)
            cell.visited = True

            neighbors = grid.get_neighbors(cell)
            walls.extend(neighbors)

            if len(neighbors) > 0:
                neighbor = random.choice(neighbors)
                if not neighbor.visited:
                    cell.link(neighbor)
                    neighbor.visited = True
                    walls.remove(neighbor)
                    walls.extend(grid.get_neighbors(neighbor))

                else:
                    walls.remove(neighbor)

