import random
from grid import Grid
from grid import Cell


class Sidewinder():
    def generate(self, grid):
        g = grid.grid

        for r in range(grid.rows - 1, 0, -1):
            run = []
            for c in range(grid.cols):
                cell = g[r][c]
                run.append(cell)

                # Check for eastern or northern boundaries
                eastmost = grid.get_east(cell) is None
                northmost = grid.get_north(cell) is None

                # Close run at the end of row or randomly within a row as
                # long as it is not the northernmost row.
                should_close = eastmost or (
                        not northmost and random.randint(0, 1) == 0)
                if should_close:
                    index = random.randint(0, len(run) - 1)
                    member = run[index]
                    north_cell = grid.get_north(member)
                    if north_cell:
                        member.link(north_cell)
                    run.clear()  # Finish a run

                else:
                    east_cell = grid.get_east(cell)
                    cell.link(east_cell)
