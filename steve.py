
#Initialize
import pygame

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Tornado!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("tc.png")
    background= pygame.transform.scale(background, (640,480))

    #load an image
    tor = pygame.image.load("ef3.png")
    tor = tor.convert_alpha()
    tor = pygame.transform.scale(tor, (200, 225))

    # set up some cardinal variables
    tor_x = 0
    tor_y = 300

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(70)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify cardinal value
        tor_x += 5
        #check boundaries
        if tor_x > screen.get_width():
            tor_x = 0

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(tor, (tor_x, tor_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()