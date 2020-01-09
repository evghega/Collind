import openpyxl
from openpyxl import Workbook
from datetime import date



def checkAnswer(answer, id, Cube):
    workbook = openpyxl.load_workbook("cards.xlsx")
    sheet = workbook.active
    if answer == sheet[Cube + str(id)].value:
        return True
    else:
        return False


def CreateGameID(user_id): #(by Tzlil) דרישה 18,22
    workbook = openpyxl.load_workbook("gameSQL.xlsx")  # getting the database location
    sheet = workbook.get_sheet_by_name('Games')
    count = 2
    while sheet['A' + str(count)].value != None:
        count = count + 1
    sheet['A' + str(count)] = count - 1
    sheet['B' + str(count)] = 0
    sheet['C' + str(count)] = 0
    sheet['D' + str(count)] = user_id
    today = date.today()
    d1 = str(today.strftime("%d.%m.%Y"))
    sheet['E' + str(count)] = d1
    workbook.save("gameSQL.xlsx")
    return True

def answertoDB(answer, gameID):
    workbook = openpyxl.load_workbook("gameSQL.xlsx")  # getting the database location
    sheet = workbook.get_sheet_by_name('Games')
    if answer:
        sheet["B"+str(gameID+1)].value += 1
        workbook.save("gameSQL.xlsx")

    else:
        sheet["C" + str(gameID+1)].value += 1
        workbook.save("gameSQL.xlsx")

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
    list = []
    for i in range(2, sheet.max_row + 1):
        if sheet['B' + str(i)].value != None:
            list.append(sheet['B' + str(i)].value)
    for i in list:
        if username == i:
            return False
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
    return True


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
            workbook = openpyxl.load_workbook("gameSQL.xlsx")
            sheet1 = workbook.get_sheet_by_name('Games')
            for j in range (2,sheet1.max_row+1):
                if sheet1['D'+str(j)].value ==i_d:
                    sheet1['A' + str(i)] = None
                    sheet1['B' + str(i)] = None
                    sheet1['C' + str(i)] = None
                    sheet1['D' + str(i)] = None
                    sheet1['E' + str(i)] = None
                    sheet1['F' + str(i)] = None
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



def gameOfDate(day,month,year): #דרישה 17
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Games')
    date = str(day) +'.'+str(month)+'.'+year
    list=[]
    for i in range(2,sheet.max_row+1):
        if str(sheet['E'+str(i)].value) ==date:
            list.append(sheet['A'+str(i)].value)
    return list


def gamesOfUser(usename): #דרישה 13,5
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet = workbook.get_sheet_by_name('Users')
    list = []
    for i in range(2,sheet.max_row+1):
        if str(sheet['B'+str(i)].value) == usename:
            i_d = sheet['A'+str(i)].value
    workbook = openpyxl.load_workbook("gameSQL.xlsx")
    sheet1 = workbook.get_sheet_by_name('Games')
    for i in range(2,sheet1.max_row+1):
        if sheet1['D'+str(i)].value == i_d:
            list.append(sheet1['A'+str(i)].value)
    return list




#addUser('neta','abcd','tzlil','levi','tzlil@com','053446','admin')
#resetUser(2)


#print(addUser('snir','123','ngame','jyj','snir@','1234','type'))
#print(gamesOfUser('admin'))

#print(gameOfDate('09','01','2020'))
answertoDB(True, 6)