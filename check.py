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
    workbook = openpyxl.load_workbook("check.xlsx")
    sheet = workbook.active

    for row in sheet.iter_rows():
        for cell in row:
            print(cell.value)
    workbook.save(filename="check.xlsx")


answertoDB(True,4)


