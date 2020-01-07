import pygame
import random
import excelfunc

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
Clock = pygame.time.Clock()
# Set the width and height of the screen [width, height]
size = (950, 600)
screen = pygame.display.set_mode(size)

# Variables
screen_Num = 0
Mouse_x = 0
Mouse_y = 0
A1_x = 100
A1_y = 450
A2_x = 300
A2_y = 450
A3_x = 500
A3_y = 450
A4_x = 600
A4_y = 450
A_wid = 150
A_hig = 100
Pause_x = 10
Pause_y = 10
Center_x = 450
Center_y = 300
GameID = 0
count = 0
font = pygame.font.Font(None, 48)

pygame.display.set_caption("Collind")


# functions
def card(Card_Num):
    if Card_Num == 1:
        img = pygame.image.load(r'CARD1.png')
    if Card_Num == 2:
        img = pygame.image.load(r'CARD2.png')
    if Card_Num == 3:
        img = pygame.image.load(r'CARD3.png')
    if Card_Num == 4:
        img = pygame.image.load(r'CARD4.png')
    if Card_Num == 5:
        img = pygame.image.load(r'CARD5.png')
    if Card_Num == 6:
        img = pygame.image.load(r'CARD6.png')
    if Card_Num == 7:
        img = pygame.image.load(r'CARD7.png')
    if Card_Num == 8:
        img = pygame.image.load(r'CARD8.png')
    else:
        img = pygame.image.load(r'CARD1.png')

    img = pygame.transform.scale(img, (int(728 / 3), int(1052 / 3)))
    screen.blit(img, (350, 50))



def click(Mouse_x, Mouse_y):
    if Mouse_x > Center_x and Mouse_x < (Center_x + A_wid) and Mouse_y > Center_y and Mouse_y < (Center_y + A_hig):
        return 0
    if Mouse_x > A1_x and Mouse_x < (A1_x + A_wid) and Mouse_y > A1_y and Mouse_y < (A1_y + A_hig):
        return 1
    if Mouse_x > A2_x and Mouse_x < (A2_x + A_wid) and Mouse_y > A2_y and Mouse_y < (A2_y + A_hig):
        return 2
    if Mouse_x > A3_x and Mouse_x < (A3_x + A_wid) and Mouse_y > A3_y and Mouse_y < (A3_y + A_hig):
        return 3
    if Mouse_x > Pause_x and Mouse_x < (Pause_x + A_wid) and Mouse_y > Pause_y and Mouse_y < (Pause_y + A_hig):
        return 4


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        Mouse_x = pos[0]
        Mouse_y = pos[1]

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
   # screen.fill(pygame.image.load(r'CARD5.png'))
    background_image = pygame.image.load("loginbackground.png").convert()
    screen.blit(background_image, [0, 0])
    # --- Drawing code should go here
    if screen_Num == 0:
        font = pygame.font.Font(None, 36)
        StartB = pygame.draw.rect(screen, BLACK, [Center_x, Center_y, A_wid, A_hig], 1)
        text = font.render("Start Game", True, BLACK)
        screen.blit(text, [Center_x + 2, Center_y + A_hig / 2])
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mouse_x, Mouse_y = event.pos
            if StartB.collidepoint(Mouse_x, Mouse_y):
                Card_Num = random.randint(1, 6)
                Cube_Num = chr(random.randrange(65, 65 + 5))
                print(Card_Num,Cube_Num)
                screen_Num = 1
                GameID = excelfunc.CreateGameID()

    elif screen_Num == 1:
        card(Card_Num)
        A1 = pygame.draw.rect(screen, BLACK, [A1_x, A1_y, A_wid, A_hig], 2)
        text = font.render("1", True, BLACK)
        screen.blit(text, [A1_x + A_wid/2, A1_y + A_hig / 2])

        A2 = pygame.draw.rect(screen, BLACK, [A2_x, A2_y, A_wid, A_hig], 2)
        text = font.render("2", True, BLACK)
        screen.blit(text, [A2_x + A_wid/2, A2_y + A_hig / 2])

        A3 = pygame.draw.rect(screen, BLACK, [A3_x, A3_y, A_wid, A_hig], 2)
        text = font.render("3", True, BLACK)
        screen.blit(text, [A3_x + A_wid/2, A3_y + A_hig / 2])

        P = pygame.draw.rect(screen, BLACK, [Pause_x, Pause_y, A_wid, A_hig], 2)
        text = font.render("Pause", True, BLACK)
        screen.blit(text, [Pause_x + 2, Pause_y + A_hig / 2])

        if event.type == pygame.MOUSEBUTTONUP:
            count = 0
        if event.type == pygame.MOUSEBUTTONDOWN and count == 0:
            Mouse_x, Mouse_y = event.pos
            if A1.collidepoint(Mouse_x, Mouse_y):
                excelfunc.answertoDB(excelfunc.checkAnswer(1, Card_Num, Cube_Num), GameID)
                print("A1")
                count = 1
            if A2.collidepoint(Mouse_x, Mouse_y):
                excelfunc.answertoDB(excelfunc.checkAnswer(2, Card_Num, Cube_Num), GameID)
                print("A2")
                count = 1
            if A3.collidepoint(Mouse_x, Mouse_y):
                excelfunc.answertoDB(excelfunc.checkAnswer(3, Card_Num, Cube_Num), GameID)
                print("A3")
                count = 1
            if P.collidepoint(Mouse_x, Mouse_y):
               screen_Num=2

    elif screen_Num == 2:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [Center_x, Center_y, A_wid, A_hig], 2)
        text = font.render("Continue?", True, BLACK)
        screen.blit(text, [Center_x + 2, Center_y + A_hig / 2])
        if click(Mouse_x, Mouse_y) == 0:
            screen_Num = 1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    Clock.tick(30)

# Close the window and quit.
pygame.quit()
