import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        pos = (0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        pos = (32*random.randrange(0, 20), 32*random.randrange(0, 16))

            screen.fill("light green")
            for i in range(1,20):
                pygame.draw.line(screen, "black", (i*32,0), (i*32,512))
                if i < 16:
                    pygame.draw.line(screen, "black", (0,i*32), (640,i*32))
            mole = pygame.image.load("mole.png")
            mole_rect = mole.get_rect(topleft=pos)
            screen.blit(mole, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
