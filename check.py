from builtins import range, str
from openpyxl import Workbook




def checkAnswer(answer, id , Cube):
    workbook = Workbook()
    sheet = workbook.active
    if answer == sheet[Cube+str(id)]:
        return True
    else:
        return False




def answertoDB(answer, gameID):
    workbook = Workbook("check.xlsx")#getting the database location
    sheet = workbook.active
    max_column = sheet.max_column
    for i in range(2,max_column+1):
        if gameID == sheet["A"+str(i)]:
            if answer == True:
                sheet["B"+str(i)]=sheet["B"+str(i)]+1
                break
            else:
                sheet["C" + str(i)] = sheet["C" + str(i)] + 1
                break

answertoDB(True,4)