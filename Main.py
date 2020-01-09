import pygame
import random
import excelfunc
from pygame.locals import *
import pygame_textinput

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
textinput = pygame_textinput.TextInput()
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
username=""
password=""
hash=""
badpassword=False
baduser=False
subScreen_num = 0 #screen 3 helper
pygame.display.set_caption("Collind")
pos=0

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

    background_image = pygame.image.load("loginbackground.png").convert()
    badpassword_image = pygame.image.load("WorngPassword.png").convert()
    baduser_image = pygame.image.load("WorngUserName.png").convert()
    screen.blit(background_image, [0, 0])
    # --- Drawing code should go here
    if screen_Num == 0: #login page
        running = True
        while running:
         print(username)
         for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    username += evt.unicode
                elif evt.key == K_BACKSPACE:
                     username = username[:-1]
                elif evt.key == K_RETURN:
                     running = False
         if(baduser):
            screen.blit(baduser_image,[0, 0])
         if (badpassword):
            screen.blit(badpassword_image, [0, 0])
         block = font.render(username, True, (0, 0, 0))
         if(not baduser and not badpassword):
          screen.blit(background_image, [0, 0])
         screen.blit(block, [350, -50+Center_y + A_hig / 2])
         pygame.display.flip()
        while not running:
            print(password)
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        baduser = False
                        badpassword = False
                        password += evt.unicode
                        hash+="*"
                    elif evt.key == K_BACKSPACE:
                        password = password[:-1]
                        hash = hash[:-1]
                    elif evt.key == K_RETURN:
                        running = True
                        tuple=excelfunc.login(username,password)
                        print(tuple[1])
                        if (tuple[0] == False):
                            screen_Num = 0
                            if(tuple[1]=='badpassword'):
                                badpassword=True
                                username=""
                                hash=""
                                password=""
                            else:
                                baduser=True
                                username = ""
                                hash= ""
                                password = ""

                        if (tuple[0] == True):
                            if (tuple[1] == 'admin'):
                                screen_Num = 1
                            if (tuple[1] == 'tester'):
                                screen_Num = 2
                            if (tuple[1] == 'user'):
                                screen_Num = 3
            if (baduser):
                screen.blit(baduser_image, [0, 0])
            if (badpassword):
                screen.blit(badpassword_image, [0, 0])
            block = font.render(hash, True, (0, 0, 0))
            block2 = font.render(username, True, (0, 0, 0))
            if (not baduser and not baduser):
             screen.blit(background_image, [0, 0])
            screen.blit(block, [350, 70 + Center_y + A_hig / 2])
            screen.blit(block2, [350, -50 + Center_y + A_hig / 2])
            pygame.display.flip()


    elif screen_Num == 1:
      manager_image=pygame.image.load("ManagerMain.png").convert()
      screen.blit(manager_image, [0, 0])
    elif screen_Num == 2:
      tester_image = pygame.image.load("TesterMain.png").convert()
      screen.blit(tester_image, [0, 0])
    elif screen_Num == 3:
      user_image = pygame.image.load("UserMain.png").convert()
      screen.blit(user_image, [0, 0])
      if event.type == pygame.MOUSEBUTTONUP:
       pos = pygame.mouse.get_pos()
      if(pos):
       print(pos)
          #the Rules Button
       if((pos[0]>235 and pos[0]<419) and (pos[1]>229 and pos[1]<296) and pygame.mouse.get_pressed()[0]):
          subScreen_num=1
          pos=False
           #The StartGame Button
       if ((pos[0] > 501 and pos[0] < 681) and (pos[1] > 238 and pos[1] < 301) and pygame.mouse.get_pressed()[0]):
           screen_Num = 4
           #Exit Func
       if ((pos[0] > 12 and pos[0] < 160) and (pos[1] > 7 and pos[1] < 42) and pygame.mouse.get_pressed()[0]):
           pygame.quit()
      if subScreen_num==1:
         rules_image = pygame.image.load("Rules.png").convert()
         screen.blit(rules_image, [0, 0])
         if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          if pos:
            print(pos)
            if((pos[0]>308 and pos[0]<418) and (pos[1]>12 and pos[1]<50)):
                subScreen_num = 0


    #Board Game!!
    elif screen_Num == 4:
        game_image = pygame.image.load("Game.png").convert()
        screen.blit(game_image, [0, 0])
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        if (pos):
            print(pos)
            # the Rules Button
            if ((pos[0] > 235 and pos[0] < 419) and (pos[1] > 229 and pos[1] < 296) and pygame.mouse.get_pressed()[0]):
                subScreen_num = 1
                pos = False


    elif screen_Num == 5:
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
