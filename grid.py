import random


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.prep_grid()
        self.configure_cells()

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
                if r + 1 > self.rows:
                    south = None
                if c - 1 < 0:
                    west = None
                if c > self.cols:
                    east = None

                self.grid[r][c].north = north
                self.grid[r][c].south = south
                self.grid[r][c].east = east
                self.grid[r][c].west = west

    def random_cell(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        return self.grid[row][col]


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
