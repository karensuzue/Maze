import media
from grid import Grid
from grid import Cell
from PIL import Image
from PIL import ImageDraw

class ToPNG():
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.cell_size = cell_size
        self.image_size = (cell_size * grid.rows, cell_size * grid.cols)
        self.wall_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)

    def render(self):
        canvas = Image.new('RGB', self.image_size, self.bg_color)
        draw = ImageDraw.Draw(canvas)

        # Draw borders:
        draw.line((0, 0, 0, self.cell_size * self.grid.rows - 1), fill=self.wall_color, width=1) # Left
        draw.line((self.cell_size * self.grid.cols - 1, 0, self.cell_size * self.grid.cols - 1, self.cell_size * self.grid.rows - 1), fill=self.wall_color, width=1) # Right
        draw.line((0, 0, self.cell_size * self.grid.cols - 1, 0), fill=self.wall_color, width=1) # Top
        draw.line((0, self.cell_size * self.grid.rows - 1, self.cell_size * self.grid.cols - 1, self.cell_size * self.grid.rows - 1), fill=self.wall_color, width=1)

        # Draw maze:
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                cell = self.grid.grid[r][c]
                # Northwest corner
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                # Southeast corner
                x2 = (c + 1) * self.cell_size
                y2 = (r + 1) * self.cell_size

                north = self.grid.get_north(cell)
                south = self.grid.get_south(cell)
                east = self.grid.get_east(cell)
                west = self.grid.get_west(cell)

                if not cell.exist_link(east):
                    draw.line((x2, y1, x2, y2), fill=self.wall_color, width=1)
                if not cell.exist_link(south):
                    draw.line((x1, y2, x2, y2), fill=self.wall_color, width=1)

        canvas.save("test.png")
        return canvas
