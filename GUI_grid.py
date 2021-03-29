import pygame
import random


class Grid:
    def __init__(self, rows, cols, screen):
        self.rows = rows
        self.cols = cols
        self.grid = self.prep_grid(screen)
        self.configure_cells()

        self.bg_color = (0, 0, 0)
        #self.screen = screen

    def get_size(self):
        # Size as in row x col
        return self.rows * self.cols

    def prep_grid(self, screen):
        grid = [[Cell(row, col, screen) for col in range(self.cols)] for
                row in range(self.rows)]
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

    def draw_cells(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                east_cell = self.get_east(cell)
                south_cell = self.get_south(cell)

                if cell.exist_link(east_cell):
                    east_cell.draw_cell()

                if cell.exist_link(south_cell):
                    south_cell.draw_cell()


class Cell:
    def __init__(self, row, col, screen):
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

        self.color = (255, 255, 255)
        self.size = 50
        self.screen = screen
        self.rect = pygame.Rect(self.row + self.size, self.col + self.size,
                                self.size, self.size)

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

    def draw_cell(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
