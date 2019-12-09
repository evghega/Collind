import openpyxl
from openpyxl import Workbook


def checkAnswer(answer, id, Cube):
    workbook = openpyxl.load_workbook("cards.xlsx")
    sheet = workbook.active
    if answer == sheet[Cube + str(id)].value:
        return True
    else:
        return False

def CreateGameID():
    workbook = openpyxl.load_workbook("check.xlsx")  # getting the database location
    sheet = workbook.active
    test="test"
    size = len(sheet['A'])
    gameid = sheet.cell(size,1).value+1
    sheet.cell(size+1, 1).value = gameid
    sheet.cell(size + 1, 2).value=0
    sheet.cell(size + 1, 3).value=0
    workbook.save("check.xlsx")
    return gameid

def answertoDB(answer, gameID):
    workbook = openpyxl.load_workbook("check.xlsx")  # getting the database location
    sheet = workbook.active
    if answer:
        sheet["B"+str(gameID+1)].value += 1
        workbook.save("check.xlsx")

    else:
        sheet["C" + str(gameID+1)].value += 1
        workbook.save("check.xlsx")
