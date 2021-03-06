import media
from PIL import Image
from PIL import ImageDraw

from grid import Grid
from grid import Cell
from image_export.dijkstra import Dijkstra


class ToPNG():
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.cell_size = cell_size
        self.image_size = (cell_size * grid.cols, cell_size * grid.rows)
        self.wall_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.dark_bg_color = ()

    def render_path(self):
        """
        Obtain and renders the solution path
        :return: a list of solution path cells
        """
        # Start solving from the southwest corner
        distance_map = Dijkstra()
        distance_map.solve(self.grid, self.grid.rows - 1, 0)

        # Walk backwards from end goal, which is northeast corner
        goal = self.grid.grid[0][self.grid.cols - 1]

        # Find solution path
        solution_path = [goal]
        temp = goal
        while temp.distance is not 1:
            links = temp.links
            for cell in links:
                if cell.distance == temp.distance - 1:
                    solution_path.append(cell)
                    temp = cell

        # Begin drawing maze:
        canvas = Image.new('RGB', self.image_size, self.bg_color)
        draw = ImageDraw.Draw(canvas)

        # Fill cell from solution path with red:
        color = (255, 0, 0)
        for i in range(len(solution_path)):
            c = solution_path[i].col
            r = solution_path[i].row

            # Northwest corner
            x1 = c * self.cell_size
            y1 = r * self.cell_size
            # Southeast corner
            x2 = (c + 1) * self.cell_size
            y2 = (r + 1) * self.cell_size

            draw.rectangle([x1, y1, x2, y2], fill=color)

        # Draw borders:
        draw.line((0, 0, 0, self.image_size[1] - 1),
                  fill=self.wall_color, width=1)  # Left
        draw.line((self.image_size[0] - 1, 0,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Right
        draw.line((0, 0, self.image_size[1] - 1, 0),
                  fill=self.wall_color, width=1)  # Top
        draw.line((0, self.image_size[1] - 1,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Bottom

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

                # north = self.grid.get_north(cell)
                south = self.grid.get_south(cell)
                east = self.grid.get_east(cell)
                # west = self.grid.get_west(cell)

                if not cell.exist_link(east):
                    draw.line((x2, y1, x2, y2), fill=self.wall_color, width=1)
                if not cell.exist_link(south):
                    draw.line((x1, y2, x2, y2), fill=self.wall_color, width=1)

        canvas.save("maze-solution.png")

        return solution_path

    def render(self):
        """
        Render a plain maze.
        :return: an image of a maze
        """
        canvas = Image.new('RGB', self.image_size, self.bg_color)
        draw = ImageDraw.Draw(canvas)

        # Draw borders:
        draw.line((0, 0, 0, self.image_size[1] - 1),
                  fill=self.wall_color, width=1)  # Left
        draw.line((self.image_size[0] - 1, 0,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Right
        draw.line((0, 0, self.image_size[1] - 1, 0),
                  fill=self.wall_color, width=1)  # Top
        draw.line((0, self.image_size[1] - 1,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Bottom

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

                # north = self.grid.get_north(cell)
                south = self.grid.get_south(cell)
                east = self.grid.get_east(cell)
                # west = self.grid.get_west(cell)

                if not cell.exist_link(east):
                    draw.line((x2, y1, x2, y2), fill=self.wall_color, width=1)
                if not cell.exist_link(south):
                    draw.line((x1, y2, x2, y2), fill=self.wall_color, width=1)

        canvas.save("maze.png")
        return canvas

    def render_color(self):
        """
        Render a colored bias map.
        :return: an image of a colored maze
        """
        canvas = Image.new('RGB', self.image_size, self.bg_color)
        draw = ImageDraw.Draw(canvas)

        # Start from the middle of the maze
        distance_map = Dijkstra()
        distance_map.solve(self.grid, self.grid.rows // 2 - 1,
                           self.grid.cols // 2 - 1)

        # Fill cell with color:
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                cell = self.grid.grid[r][c]
                color = distance_map.color_for_cell(cell)

                # Northwest corner
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                # Southeast corner
                x2 = (c + 1) * self.cell_size
                y2 = (r + 1) * self.cell_size

                draw.rectangle([x1, y1, x2, y2], fill=color)

        # Draw maze outline:
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                cell = self.grid.grid[r][c]

                # Northwest corner
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                # Southeast corner
                x2 = (c + 1) * self.cell_size
                y2 = (r + 1) * self.cell_size

                # north = self.grid.get_north(cell)
                south = self.grid.get_south(cell)
                east = self.grid.get_east(cell)
                # west = self.grid.get_west(cell)

                if not cell.exist_link(east):
                    draw.line((x2, y1, x2, y2), fill=self.wall_color, width=1)
                if not cell.exist_link(south):
                    draw.line((x1, y2, x2, y2), fill=self.wall_color, width=1)

        # Draw borders:
        draw.line((0, 0, 0, self.image_size[1] - 1),
                  fill=self.wall_color, width=1)  # Left
        draw.line((self.image_size[0] - 1, 0,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Right
        draw.line((0, 0, self.image_size[1] - 1, 0),
                  fill=self.wall_color, width=1)  # Top
        draw.line((0, self.image_size[1] - 1,
                   self.image_size[0] - 1,
                   self.image_size[1] - 1), fill=self.wall_color,
                  width=1)  # Bottom

        canvas.save("maze-colored.png")
        return canvas

    def render_path2(self):
        """
        Obtain the solution path without rendering.
        :return: a list of cells in solution path
        """
        # Start solving from the southwest corner
        distance_map = Dijkstra()
        distance_map.solve(self.grid, self.grid.rows - 1, 0)

        # Walk backwards from end goal, which is northeast corner
        goal = self.grid.grid[0][self.grid.cols - 1]

        # Find solution path
        solution_path = [goal]
        temp = goal
        while temp.distance is not 1:
            links = temp.links
            for cell in links:
                if cell.distance == temp.distance - 1:
                    solution_path.append(cell)
                    temp = cell

        return solution_path
