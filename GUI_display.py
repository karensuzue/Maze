import pygame
from GUI_grid import Grid
from binary_tree import BinaryTree

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Maze Solver and Generator")
    grid = Grid(4, 4, screen)

    running = True
    while running:
        #screen.fill((255, 255, 200))
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            BinaryTree().generate(grid)
            grid.draw_cells()



        pygame.display.update()



if __name__ == "__main__":
    main()
