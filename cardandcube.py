from random import randint
import openpyxl
import pygame


def cube():
    
    num = randint(1,6)

    if (num == 1):
        return (pygame.image.load("items\CUBES.png"), 'B')
    if (num == 2):
        return (pygame.image.load("items\CUBEC.png"), 'C')
    if (num == 3):
        return (pygame.image.load("items\CUBER.png"), 'D')
    if (num == 4):
        return (pygame.image.load("items\CUBEL.png"), 'E')
    if (num == 5):
        return (pygame.image.load("items\CUBEY.png"), 'F')
    if (num == 6):
        return (pygame.image.load("items\CUBEM.png"), 'G')


def cardenablef(ID):
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Cards')
    if sheet['I' + str(ID+2)].value == 'yes':
        return True
    else:
        return False

def card():
    ID=0
    while(not cardenablef(ID)):
     card = randint(1,8)
     ID = randint(1, 8)
    if(card==1):
        return (pygame.image.load("items\CARD1.png"),1)
    if(card==2):
        return (pygame.image.load("items\CARD2.png"),2)
    if(card==3):
        return (pygame.image.load("items\CARD3.png"),3)
    if(card==4):
        return (pygame.image.load("items\CARD4.png"),4)
    if(card==5):
        return (pygame.image.load("items\CARD5.png"),5)
    if(card==6):
        return (pygame.image.load("items\CARD6.png"),6)
    if (card == 7):
        return (pygame.image.load("items\CARD7.png"),7)
    if (card == 8):
        return (pygame.image.load("items\CARD8.png"),8)


