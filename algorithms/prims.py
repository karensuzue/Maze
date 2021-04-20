import random
from grid import Grid
from grid import Cell

class Prim():
    def find_unvisited_neighbors(self, cell, grid):
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
        first = grid.random_cell()
        path = [first]
        while len(path) > 0:
            cell = random.choice(path)
            cell.visited = True

            visited_neighbors =
            available_neighbors = self.find_neighbors(cell, grid)
            if len(available_neighbors) > 0:
                neighbor = random.choice(available_neighbors)
                cell.link(neighbor)

                neighbors_of_neighbor = self.find_neighbors(neighbor, grid)
                for i in range(len(neighbors_of_neighbor)):
                    if neighbors_of_neighbor[i] not in path:
                            path.append(neighbors_of_neighbor[i])


            path.remove(cell)









    def generate3(self, grid):
        # Arbitrary starting cell
        first = grid.random_cell()
        frontier = [first]
        maze = []

        while len(frontier) > 0:
            cell = random.choice(frontier)
            maze.append(cell)
            frontier.remove(cell)
            available_neighbors = self.find_neighbors(cell, grid)
            print(available_neighbors)

            # Avoid duplicates in frontier set
            for i in range(len(available_neighbors)):
                if available_neighbors[i] not in (frontier or maze):
                    frontier.append(available_neighbors[i])

            if len(available_neighbors) > 0:
                for i in range(len(maze)):
                    if maze[i] in available_neighbors:
                        cell.link(maze[i])
                        break




    def generate2(self, grid):
        # Arbitrary starting cell
        first = grid.random_cell()
        frontier = [first]
        maze = []

        # Assign random costs to each cell (not edges)
        costs = {}
        for r in range(grid.rows):
            for c in range(grid.cols):
                cell = grid.grid[r][c]
                costs[cell] = random.randint(1, 100)

        while len(frontier) > 0:
            cell = self.min_element(frontier, costs)  # Cell with minimum cost
            maze.append(cell)
            available_neighbors = self.find_neighbors(cell, grid)

            # Avoid duplicates in frontier set
            for i in range(len(available_neighbors)):
                if available_neighbors[i] not in (frontier and maze):
                    frontier.append(available_neighbors[i])

            for i in range(len(maze)):
                if maze[i] in available_neighbors:
                    cell.link(maze[i])
                    frontier.remove(cell)
            print(frontier)