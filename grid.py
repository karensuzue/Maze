class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Neighbors
        # Knowledge of invalid neighboring cells depends on the grid, so
        # that will be taken care of in the Grid class
        self.north = (row + 1, col)
        self.south = (row - 1, col)
        self.east = (row, col + 1)
        self.west = (row, col - 1)

        # Linked/joined cells
        self.links = {}

    def link(self, cell):
        """
        Connects current cell with another cell.
        :param cell:
        :return:
        """

    def unlink(self, cell):
        """
        Disconnects current cell with another cell.
        :param cell:
        :return:
        """

    def get_all_links(self):
        """
        Get a list of all cells connected to current cell.
        :return:
        """

    def exist_link(self, cell):
        """
        Check to see if current cell is connected to the parameter cell.
        :return:
        """
        linked = False
        return linked

    def get_neighbors(self):
        """
        Get list of neighboring, but not necessarily connected cells.
        :return:
        """
        neighbors = []

