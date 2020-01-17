
import pygame
import excelfunc
import cardandcube
from pygame.locals import *
import Admin_user_edit
import wordInput
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
#textinput = pygame.TextInput()
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
pos1=0
cardenable=False
cubeenable=False
card_image=None
cube_image=None
cubenum=0
cardnum=0
pauseenable=False
usersenable =False
reportenable=False
feedbackenable=False
# functions
tempscreen=0
def checkscreen(n):
    global tempscreen
    tempscreen=n
def ClickBack1():
    return 1
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

    background_image = pygame.image.load("items\loginbackground.png").convert()
    badpassword_image = pygame.image.load("items\WorngPassword.png").convert()
    baduser_image = pygame.image.load("items\WorngUserName.png").convert()
    pause_image = pygame.image.load("items\pause.png").convert()
    users_image = pygame.image.load(r"items\users.png").convert()
    items_image = pygame.image.load("items\items.png").convert()
    # --- Drawing code should go here
    if screen_Num == 0: #login page
        screen.blit(background_image, [0, 0])
        running = True
        ################EnterDetails############
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
                        tuple=excelfunc.checkDetails(username,password)
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
    ################EnterDetails############

    elif screen_Num == 1:
      checkscreen(1)
      manager_image=pygame.image.load("items\ManagerMain.png").convert()
      screen.blit(manager_image, [0, 0])
      if reportenable:
          report_image = pygame.image.load(r"items\report.png").convert()
          screen.blit(report_image, [0, 0])
          screen_Num=9
      if(usersenable):
          screen.blit(users_image, [0, 0])
          screen_Num=8
      pygame.display.update()
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
       pos = pygame.mouse.get_pos()
       if(pos):
        print(pos)
          #items
        if((pos[0]>675 and pos[0]<855) and (pos[1]>220 and pos[1]<296)):
           screen_Num=10
           print("Enter Items Screen")
           #users
        if ((pos[0] > 440 and pos[0] < 620) and (pos[1] > 220 and pos[1] < 296)):
           usersenable=True
           #reports
        if ((pos[0] > 170 and pos[0] < 349) and (pos[1] > 220 and pos[1] < 290) ):
           reportenable=True
           #startgame
        if ((pos[0] > 323 and pos[0] < 504) and (pos[1] > 350 and pos[1] < 422)):
           screen_Num=4
           gameid = excelfunc.CreateGameID(userid)
           print(gameid)
           countans = 0
           cardnum = 0
           cubenum = 0
        if ((pos[0] > 12 and pos[0] < 160) and (pos[1] > 7 and pos[1] < 42)):
           screen_Num=0
           hash=""
           username=""
           password=""
        pos=False
    elif screen_Num==8:
          pygame.display.update()
          Admin_user_edit.action_list()
          usersenable=False
          screen_Num=tempscreen


        #items Screen
    elif screen_Num == 10:
     pygame.display.update()
     screen.blit(items_image, [0, 0])
     if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
        pos = pygame.mouse.get_pos()
        if (pos):
        #1
         if ((pos[0] > 861 and pos[0] < 923) and (pos[1] > 103 and pos[1] < 154)):
            excelfunc.Card_enable(1)
            print("change card state to yes")
         if ((pos[0] > 861 and pos[0] < 923) and (pos[1] > 174 and pos[1] < 228)):
            excelfunc.Card_enable(1)
            print("change card state to no")
        #2
         if ((pos[0] > 660 and pos[0] < 718) and (pos[1] > 103 and pos[1] < 154) ):
            excelfunc.Card_enable(2)
            print("change card state to yes")
         if ((pos[0] > 660 and pos[0] < 718) and (pos[1] > 174 and pos[1] < 228) ):
            excelfunc.Card_enable(2)
            print("change card state to no")

        #3
         if ((pos[0] > 406 and pos[0] < 459) and (pos[1] > 103 and pos[1] < 154) ):
            excelfunc.Card_enable(3)
            print("change card state to yes")
         if ((pos[0] > 406 and pos[0] < 459) and (pos[1] > 174 and pos[1] < 228) ):
            excelfunc.Card_enable(3)
            print("change card state to no")
        #4
         if ((pos[0] > 201 and pos[0] <270) and (pos[1] > 103 and pos[1] < 154) ):
            excelfunc.Card_enable(4)
            print("change card state to yes")
         if ((pos[0] > 201 and pos[0] < 270) and (pos[1] > 174 and pos[1] < 228)):
            excelfunc.Card_enable(4)
            print("change card state to no")
        #5
         if ((pos[0] > 869 and pos[0] < 940) and (pos[1] > 306 and pos[1] < 362) ):
            excelfunc.Card_enable(5)
            print("change card state to yes")
         if ((pos[0] > 869 and pos[0] < 940) and (pos[1] > 338 and pos[1] < 431) ):
            excelfunc.Card_enable(5)
            print("change card state to no")

        #6
         if ((pos[0] > 667 and pos[0] < 726) and (pos[1] > 306 and pos[1] < 362) ):
            excelfunc.Card_enable(6)
            print("change card state to yes")
         if ((pos[0] > 675 and pos[0] < 855) and (pos[1] > 338 and pos[1] < 431) ):
            excelfunc.Card_enable(6)
            print("change card state to no")
        #7
         if ((pos[0] > 399 and pos[0] < 466) and (pos[1] > 306 and pos[1] < 362) ):
            excelfunc.Card_enable(7)
            print("change card state to yes")
         if ((pos[0] > 403 and pos[0] < 466) and (pos[1] > 338 and pos[1] < 431) ):
            excelfunc.Card_enable(7)
            print("change card state to no")
        #8
         if ((pos[0] > 191 and pos[0] < 255) and (pos[1] > 306 and pos[1] < 362) ):
            excelfunc.Card_enable(8)
            print("change card state to yes")
         if ((pos[0] > 191 and pos[0] < 255) and (pos[1] > 338 and pos[1] < 431) ):
            excelfunc.Card_enable(8)
            print("change card state to no")
        #Exit
         if ((pos[0] > 19 and pos[0] < 153) and (pos[1] > 10 and pos[1] < 82)):
            screen_Num = ClickBack1()
         pos = False
    elif screen_Num == 2:
      checkscreen(2)
      tester_image = pygame.image.load("items\TesterMain.png").convert()
      screen.blit(tester_image, [0, 0])
      if reportenable:
          report_image = pygame.image.load(r"items\report.png").convert()
          screen.blit(report_image, [0, 0])
          screen_Num = 9
      if (usersenable):
          screen.blit(users_image, [0, 0])
          screen_Num = 8
      if event.type == pygame.MOUSEBUTTONDOWN:
       pos = pygame.mouse.get_pos()
       if(pos):
        print(pos)
          #users
        if((pos[0]>513 and pos[0]<691) and (pos[1]>236 and pos[1]<296)):
           usersenable = True
           # reports
        if ((pos[0] > 237 and pos[0] < 419) and (pos[1] > 234 and pos[1] < 292) ):
           reportenable = True
           # startgame
        if ((pos[0] > 393 and pos[0] < 574) and (pos[1] > 370 and pos[1] < 439) ):
           screen_Num = 4
           gameid = excelfunc.CreateGameID(userid)
           print(gameid)
           countans = 0
           cardnum = 0
           cubenum = 0
        if ((pos[0] > 12 and pos[0] < 160) and (pos[1] > 7 and pos[1] < 42) ):
           screen_Num = 0
           hash = ""
           username = ""
           password = ""
        pos= False


    elif screen_Num == 3:
      checkscreen(3)
      user_image = pygame.image.load(r"items\UserMain.png").convert()
      screen.blit(user_image, [0, 0])
      if event.type == pygame.MOUSEBUTTONDOWN:
       pos = pygame.mouse.get_pos()
       if(pos):
        print(pos)
          #the Rules Button guideClicked
        if((pos[0]>235 and pos[0]<419) and (pos[1]>229 and pos[1]<296) ):
          subScreen_num=1
         # pos=False
           #The StartGame Button
        if ((pos[0] > 501 and pos[0] < 681) and (pos[1] > 238 and pos[1] < 301) ):
           screen_Num = 4
           gameid=excelfunc.CreateGameID(userid)
           print(gameid)
           countans = 0
           cardnum=0
           cubenum=0
           #Exit Func
        if ((pos[0] > 12 and pos[0] < 160) and (pos[1] > 7 and pos[1] < 42) ):
           screen_Num = 0
           hash = ""
           username = ""
           password = ""
      if subScreen_num==1: #guides    28.2
         rules_image = pygame.image.load("items\Rules.png").convert()
         screen.blit(rules_image, [0, 0])
         if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          if pos:
            print(pos)
            if((pos[0]>308 and pos[0]<418) and (pos[1]>12 and pos[1]<50)):
                subScreen_num = 0


    #Board Game!!
    elif screen_Num == 4:
        cardid=0
        game_image = pygame.image.load("items\Game.png").convert()
        screen.blit(game_image, [0, 0])
        if(countans>=8): #endGame
            #game is over
            feedbackenable=True


        if event.type == pygame.MOUSEBUTTONDOWN :
         pos = pygame.mouse.get_pos()
         if (pos):
            print(pos)
            # pull card ########execute NextCard inside func of pygame############
            if ((pos[0] > 708 and pos[0] < 838) and (pos[1] > 537 and pos[1] < 571)):
              card_image= cardandcube.card()[0]
              cardnum = cardandcube.card()[1]
              cardenable=True
            #pull cube  ##########cubeclicked###########
            if ((pos[0] > 400 and pos[0] < 595) and (pos[1] > 309 and pos[1] < 346)):
              cube_tuple= cardandcube.cube()
              cube_image=cube_tuple[0]
              cubenum=cube_tuple[1]
              cubeenable=True
            #answer1
            if ((pos[0] > 118 and pos[0] < 243) and (pos[1] > 412 and pos[1] < 594)):
                 print("1")
                 print(cardnum,cubenum)
                 excelfunc.answertoDB(excelfunc.checkAnswer(1,cardnum,cubenum),gameid)
                 countans+=1
            # answer2
            if ((pos[0] > 280 and pos[0] < 412) and (pos[1] > 411 and pos[1] < 594) ):
                 excelfunc.answertoDB(excelfunc.checkAnswer(2,cardnum,cubenum),gameid)
                 print("2")
                 print(cardnum, cubenum)
                 countans += 1
            # answer3
            if ((pos[0] > 458and pos[0] < 580) and (pos[1] > 412 and pos[1] < 594) ):
                 excelfunc.answertoDB(excelfunc.checkAnswer(3,cardnum,cubenum),gameid)
                 print("3")
                 print(cardnum, cubenum)
                 countans += 1
            #Back Button
            if ((pos[0] > 19 and pos[0] < 153) and (pos[1] > 38 and pos[1] < 82) ):
                screen_Num=tempscreen
            #pause Button pause pause pause Func
            if ((pos[0] > 178 and pos[0] < 311) and (pos[1] > 41 and pos[1] < 82) ):
                pauseenable=True
            #coninto button
            if ((pos[0] > 345 and pos[0] < 695) and (pos[1] > 138 and pos[1] < 244) ):
                pauseenable=False
            pos = False
        pos = False
        if (cardenable):
            screen.blit(card_image, [600, 65])
        if (cubeenable):
            screen.blit(cube_image, [355, 91])
        if (pauseenable): #resumeExe resumeExe resumeExe resumeExe
            screen.blit(pause_image, [300, 107])
        if feedbackenable: #dbAndFeedBack29.2
            feed_image = pygame.image.load(r"items\feedback.png").convert()
            screen.blit(feed_image, [0, 0])
            screen_Num = 6
    elif screen_Num == 9:
        report_image = pygame.image.load(r"items\report.png").convert()
        screen.blit(report_image, [0, 0])
        wordInput.menu()
        screen_Num=tempscreen
        reportenable=False


    elif screen_Num == 6:
        feed_image = pygame.image.load(r"items\feedback.png").convert()
        screen.blit(feed_image, [0, 0])
        excelfunc.feedback(gameid)
        screen_Num=5
    #game is over
    elif screen_Num == 5:
        end_image = pygame.image.load("items\end.png").convert()
        screen.blit(end_image, [0, 0])
        if event.type == pygame.MOUSEBUTTONDOWN:
         pos = pygame.mouse.get_pos()
         if (pos):
          print(pos)
         # EXIT
          if ((pos[0] > 279 and pos[0] < 698) and (pos[1] > 298 and pos[1] < 423)):
             pygame.quit()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    Clock.tick(30)

# Close the window and quit.
pygame.quit()
