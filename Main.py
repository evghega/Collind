import pygame
import random
import excelfunc
import cardandcube
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
cardenable=False
cubeenable=False
card_image=None
cube_image=None
cubenum=0
cardnum=0
pauseenable=False
# functions

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
    pause_image = pygame.image.load("pause.png").convert()
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
                                userid=tuple[2]
                            if (tuple[1] == 'tester'):
                                screen_Num = 2
                                userid = tuple[2]
                            if (tuple[1] == 'user'):
                                screen_Num = 3
                                userid = tuple[2]
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
      tempscreen = 1
      manager_image=pygame.image.load("ManagerMain.png").convert()
      screen.blit(manager_image, [0, 0])
      if event.type == pygame.MOUSEBUTTONUP:
       pos = pygame.mouse.get_pos()
      if(pos):
       print(pos)
          #items
       if((pos[0]>675 and pos[0]<855) and (pos[1]>220 and pos[1]<296) and pygame.mouse.get_pressed()[0]):

           #users
       if ((pos[0] > 440 and pos[0] < 620) and (pos[1] > 220 and pos[1] < 296) and pygame.mouse.get_pressed()[0]):
           #reports
       if ((pos[0] > 170 and pos[0] < 349) and (pos[1] > 220 and pos[1] < 290) and pygame.mouse.get_pressed()[0]):

           #startgame
       if ((pos[0] > 323 and pos[0] < 504) and (pos[1] > 350 and pos[1] < 422) and pygame.mouse.get_pressed()[0]):
           screen_Num=4

    elif screen_Num == 2:
      tempscreen = 2
      tester_image = pygame.image.load("TesterMain.png").convert()
      screen.blit(tester_image, [0, 0])
    elif screen_Num == 3:
      tempscreen=3
      user_image = pygame.image.load("UserMain.png").convert()
      screen.blit(user_image, [0, 0])
      if event.type == pygame.MOUSEBUTTONUP:
       pos = pygame.mouse.get_pos()
      if(pos):
       print(pos)
          #the Rules Button
       if((pos[0]>235 and pos[0]<419) and (pos[1]>229 and pos[1]<296) and pygame.mouse.get_pressed()[0]):
          subScreen_num=1
         # pos=False
           #The StartGame Button
       if ((pos[0] > 501 and pos[0] < 681) and (pos[1] > 238 and pos[1] < 301) and pygame.mouse.get_pressed()[0]):
           screen_Num = 4
           gameid=excelfunc.CreateGameID(userid)
           print(gameid)
           countans = 0
           cardnum=0
           cubenum=0
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
        cardid=0
        game_image = pygame.image.load("Game.png").convert()
        screen.blit(game_image, [0, 0])
        if(countans==8):
            #game is over
             print("Game Is Over")
             screen_Num =5
        if(cardenable):
            screen.blit(card_image, [600, 65])
        if (cubeenable):
            screen.blit(cube_image, [355, 91])
        if (pauseenable):
            screen.blit(pause_image, [300, 107])
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        if (pos):
            print(pos)
            # pull card
            if ((pos[0] > 708 and pos[0] < 838) and (pos[1] > 537 and pos[1] < 571)):
              card_image= cardandcube.card()[0]
              cardnum = cardandcube.card()[1]
              cardenable=True
            #pull cube
            if ((pos[0] > 400 and pos[0] < 595) and (pos[1] > 309 and pos[1] < 346)):
              cube_image= cardandcube.cube()[0]
              cubenum=cardandcube.cube()[1]
              cubeenable=True
            #answer1
            if ((pos[0] > 118 and pos[0] < 243) and (pos[1] > 412 and pos[1] < 594)):
                 print("1")
                 print(cardnum,cubenum)
                 excelfunc.answertoDB(excelfunc.checkAnswer(1,cardnum,cubenum),gameid)
                 countans+=1
            # answer2
            if ((pos[0] > 280 and pos[0] < 412) and (pos[1] > 411 and pos[1] < 594) and pygame.mouse.get_pressed()[0]):
                 excelfunc.answertoDB(excelfunc.checkAnswer(2,cardnum,cubenum),gameid)
                 print("2")
                 print(cardnum, cubenum)
                 countans += 1
            # answer3
            if ((pos[0] > 458and pos[0] < 580) and (pos[1] > 412 and pos[1] < 594) and pygame.mouse.get_pressed()[0]):
                 excelfunc.answertoDB(excelfunc.checkAnswer(3,cardnum,cubenum),gameid)
                 print("3")
                 print(cardnum, cubenum)
                 countans += 1
            #Back Button
            if ((pos[0] > 19 and pos[0] < 153) and (pos[1] > 38 and pos[1] < 82) and pygame.mouse.get_pressed()[0]):
                screen_Num=tempscreen
            #pause Button
            if ((pos[0] > 178 and pos[0] < 311) and (pos[1] > 41 and pos[1] < 82) and pygame.mouse.get_pressed()[0]):
                pauseenable=True
            #coninto button
            if ((pos[0] > 345 and pos[0] < 695) and (pos[1] > 138 and pos[1] < 244) and pygame.mouse.get_pressed()[0]):
                pauseenable=False
            pos = False


    #game is over
    elif screen_Num == 5:
        end_image = pygame.image.load("end.png").convert()
        screen.blit(end_image, [0, 0])
        if event.type == pygame.MOUSEBUTTONUP:
         pos = pygame.mouse.get_pos()
        if (pos):
         print(pos)
         # EXIT
         if ((pos[0] > 279 and pos[0] < 698) and (pos[1] > 298 and pos[1] < 423)):
             pygame.quit()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    Clock.tick(20)

# Close the window and quit.
pygame.quit()
