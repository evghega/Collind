import openpyxl
from openpyxl import Workbook




def checkAnswer(answer, id , Cube):
    workbook = Workbook()
    sheet = workbook.active
    if answer == sheet["Cubeid"]:
        return True
    else:
        return False

def answertoDB(answer, gameID):
    workbook = Workbook("check.xlsx")
    sheet = workbook.active
    numID = 1
    num = 2
    while sheet["A"+str(num)] != None and sheet["A"+str(num)] == numID:
        numID = numID+1
        num=num+1
    sheet["A"+str(num)]=numID
    if answer == True:
        sheet["B"+str(num)] = sheet["B"+str(num)]+1
    else:
        sheet["C"+str(num)] = sheet["C"+str(num)] + 1

    workbook.save(filename="check.xlsx")


answertoDB(True,4)