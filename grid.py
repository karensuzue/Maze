import random


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.prep_grid()
        self.configure_cells()

    def get_size(self):
        return self.rows * self.cols

    def prep_grid(self):
        grid = [[Cell(row, col) for col in range(self.cols)] for row in
                range(self.rows)]
        return grid

    def configure_cells(self):
        for r in range(self.rows):
            for c in range(self.cols):
                north = (r - 1, c)
                south = (r + 1, c)
                east = (r, c + 1)
                west = (r, c - 1)

                if r - 1 < 0:
                    north = None
                if r + 1 > self.rows - 1:
                    south = None
                if c - 1 < 0:
                    west = None
                if c + 1 > self.cols - 1:
                    east = None

                self.grid[r][c].north = north
                self.grid[r][c].south = south
                self.grid[r][c].east = east
                self.grid[r][c].west = west

    def random_cell(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        return self.grid[row][col]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def get_east(self, cell):
        east_cell = None
        if cell.east is not None:
            row = cell.east[0]
            col = cell.east[1]
            east_cell = self.get_cell(row, col)
        return east_cell

    def get_west(self, cell):
        west_cell = None
        if cell.west is not None:
            row = cell.west[0]
            col = cell.west[1]
            west_cell = self.get_cell(row, col)
        return west_cell

    def get_north(self, cell):
        north_cell = None
        if cell.north is not None:
            row = cell.north[0]
            col = cell.north[1]
            north_cell = self.get_cell(row, col)
        return north_cell

    def get_south(self, cell):
        south_cell = None
        if cell.south is not None:
            row = cell.south[0]
            col = cell.south[1]
            south_cell = self.get_cell(row, col)
        return south_cell

    def get_turns(self):
        turns = 0
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                north = self.get_north(cell)
                south = self.get_south(cell)
                east = self.get_east(cell)
                west = self.get_west(cell)

                if cell.exist_link(north) and not cell.exist_link(south):
                    if cell.exist_link(east) and not cell.exist_link(west):
                        turns += 1

                    if cell.exist_link(west) and not cell.exist_link(east):
                        turns += 1

                if cell.exist_link(south) and not cell.exist_link(north):
                    if cell.exist_link(east) and not cell.exist_link(west):
                        turns += 1

                    if cell.exist_link(west) and not cell.exist_link(east):
                        turns += 1

        return turns

    def get_straightaways(self):
        # Cell only linked to its West-East or North-South neighbors
        straightaways = 0
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                north = self.get_north(cell)
                south = self.get_south(cell)
                east = self.get_east(cell)
                west = self.get_west(cell)

                if cell.exist_link(east) and not (
                        cell.exist_link(north) or cell.exist_link(south)):
                    if cell.exist_link(west):
                        straightaways += 1

                if cell.exist_link(north) and not (
                        cell.exist_link(east) or cell.exist_link(west)):
                    if cell.exist_link(south):
                        straightaways += 1

        return straightaways

    def get_tjunctions(self):
        junctions = 0
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                north = self.get_north(cell)
                south = self.get_south(cell)
                east = self.get_east(cell)
                west = self.get_west(cell)

                if cell.exist_link(north) and cell.exist_link(south):
                    if cell.exist_link(west) and not cell.exist_link(east):
                        junctions += 1

                    if cell.exist_link(east) and not cell.exist_link(west):
                        junctions += 1

                if cell.exist_link(west) and cell.exist_link(east):
                    if cell.exist_link(north) and not cell.exist_link(south):
                        junctions += 1

                    if cell.exist_link(south) and not cell.exist_link(north):
                        junctions += 1

        return junctions

    def get_crossroads(self):
        # Also called cross-junctions
        crossroads = 0
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                north = self.get_north(cell)
                south = self.get_south(cell)
                east = self.get_east(cell)
                west = self.get_west(cell)

                if cell.exist_link(north) and cell.exist_link(south) and cell.exist_link(east) and cell.exist_link(west):
                    crossroads += 1

        return crossroads

    def get_terminals(self):
        terminal = 0
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                north = self.get_north(cell)
                south = self.get_south(cell)
                east = self.get_east(cell)
                west = self.get_west(cell)

                if cell.exist_link(north) and not (cell.exist_link(south) or cell.exist_link(east) or cell.exist_link(west)):
                    terminal += 1

                if cell.exist_link(south) and not (cell.exist_link(north) or cell.exist_link(east) or cell.exist_link(west)):
                    terminal += 1

                if cell.exist_link(east) and not (cell.exist_link(north) or cell.exist_link(south) or cell.exist_link(west)):
                    terminal += 1

                if cell.exist_link(west) and not (cell.exist_link(north) or cell.exist_link(south) or cell.exist_link(east)):
                    terminal += 1

        return terminal

    def traverse_count(self):
        count = 0
        return count

    def get_neighbors(self, cell):
        north = self.get_north(cell)
        south = self.get_south(cell)
        east = self.get_east(cell)
        west = self.get_west(cell)

        neighbors = []
        if north is not None:
            neighbors.append(north)

        if south is not None:
            neighbors.append(south)

        if east is not None:
            neighbors.append(east)

        if west is not None:
            neighbors.append(west)

        return neighbors

    def get_edges(self):
        edges = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                east = self.get_east(cell)
                south = self.get_south(cell)

                if east is not None:
                    edges.append((cell, east))

                if south is not None:
                    edges.append((cell, south))
        return edges

    def print_grid(self):
        # each cell is 3x3 spaces/newlines
        maze_output = "+---" * self.cols + "+" + "\n"
        for r in range(self.rows):
            top = "|"
            bottom = "+"
            for c in range(self.cols):
                cell = self.grid[r][c]
                east = "|"
                south = "---"
                corner = "+"
                body = "   "

                east_cell = self.get_east(cell)
                south_cell = self.get_south(cell)

                if cell.exist_link(east_cell):
                    east = " "
                top += body + east

                if cell.exist_link(south_cell):
                    south = "   "
                bottom += south + corner

            maze_output += top + "\n"
            maze_output += bottom + "\n"

        print(maze_output)

    def maze_bit_map(self):
        map = [[0 for col in range(self.cols)] for row in
                range(self.rows)]

        return map


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Positions for neighbors
        # Knowledge of invalid neighboring cells depends on the grid, so
        # that will be dealt with in the Grid class
        # Change this to T/F depending on whether they exist? or to Cell type
        # objects
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        # Linked/joined cells
        self.links = {}
        
        self.visited = False

    def link(self, cell):
        """
        Connects current cell with another cell. (BI DIRECTIONAL)
        :param cell:
        :return:
        """
        self.links[cell] = True
        cell.links[self] = True

    def unlink(self, cell):
        """
        Disconnects current cell with another cell. (BI DIRECTIONAL)
        :param cell:
        :return:
        """

        self.links.pop(cell)
        cell.links.pop(self)

    def get_all_links(self):
        """
        Get a list of all cells connected to current cell.
        :return:
        """
        return self.links

    def exist_link(self, cell):
        """
        Check to see if current cell is connected to the parameter cell.
        :return:
        """
        linked = False
        if cell in self.links:
            linked = True
        return linked

    def get_neighbors(self):
        """
        Get list of neighboring, but not necessarily connected cells.
        :return:
        """
        neighbors = []
