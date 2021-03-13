import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Maze Solver and Generator")

    running = True
    while running:
        screen.fill((255, 255, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
