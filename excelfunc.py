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

def login(user,password):  #דרישה 1, 11,21
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Users')
    for i in range(2,sheet.max_row+1):
        if sheet['B'+str(i)].value == user:
            if sheet['C'+str(i)].value == password:
                return (True,sheet['H'+str(i)].value)
            else:
                return (False,'badpassword')
    return (False,'badusername')


def addUser(username,password,name,lastname,email,phone,type):  #דרישה: 12,3
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Users')
    count=2
    while sheet['A' + str(count)].value != None:
        count = count+1

    sheet['A'+str(count)] = count-1
    sheet['B' + str(count)] = username
    sheet['C' + str(count)] = password
    sheet['D' + str(count)] = name
    sheet['E' + str(count)] = lastname
    sheet['F' + str(count)] = email
    sheet['G' + str(count)] = phone
    sheet['H' + str(count)] = type
    workbook.save("gameSQL.xlsx")


def deleteUser(i_d):  #דרישה 7,15
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Users')
    for i in range(2,sheet.max_row+1):
        if sheet['A' + str(i)].value == i_d:
            sheet['A' + str(i)] = None
            sheet['B' + str(i)] = None
            sheet['C' + str(i)] = None
            sheet['D' + str(i)] = None
            sheet['E' + str(i)] = None
            sheet['F' + str(i)] = None
            sheet['G' + str(i)] = None
            sheet['H' + str(i)] = None
            workbook.save("gameSQL.xlsx")
            return "true"
    return 'False'

def resetUser(i_d): #דרישה 16
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Games')
    for i in range(2,sheet.max_row+1):
        if sheet['D' + str(i)].value == i_d:
            sheet['A' + str(i)] = None
            sheet['B' + str(i)] = None
            sheet['C' + str(i)] = None
            sheet['D' + str(i)] = None
            workbook.save("gameSQL.xlsx")



#addUser('neta','abcd','tzlil','levi','tzlil@com','053446','admin')
#resetUser(2)