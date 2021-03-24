for r in range(self.rows):

    for c in range(self.cols):
        if c == self.cols - 1:
            print("|" + "   " + "|", end="\n")
        else:
            if self.grid[r][c].exist_link(self.grid[r][c].east):
                c += 1
            else:
                print("|", end="   ")

print("+---" * self.cols + "+")

r = c = 0
print("+---" * self.cols + "+")

while r < self.rows:
    c = 0

    while c < self.cols:
        if c == self.cols - 1:
            print("|" + "   " + "|", end="\n")
            print("+---" * self.cols + "+")
        else:
            if self.grid[r][c].exist_link(self.grid[r][c].east):
                c += 1

            if self.grid[r][c].exist_link(self.grid[r][c].south):
                r += 1
            else:
                print("|", end="   ")

        c += 1

    r += 1

    def print_grid(self):
        # each cell is 3x3 spaces/newlines
        maze_output = ["+---" * self.cols + "+" + "\n"]
        for r in range(self.rows):
            maze_row = ["|"]
            for c in range(self.cols):
                if self.grid[r][c].east in self.grid[r][c].links:
                    maze_row.append("   ")
                else:
                    maze_row.append("   " + "|")

            maze_row.append("\n")
            maze_output.extend(maze_row)

            maze_row = ["+"]
            for c in range(self.cols):
                if self.grid[r][c].south in self.grid[r][c].links:
                    maze_row.append("   " + "+")
                else:
                    maze_row.append("---" + "+")
            maze_row.append("\n")
            maze_output.extend(maze_row)

        for i in range(len(maze_output)):
            print(maze_output[i], end="")

