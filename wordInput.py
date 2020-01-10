from docxtpl import DocxTemplate
import docx


def wordInput(name, date, num1, num2):
    if num2 < 2:
        rep = 'Your color vision regarded as normal. ' \
              'You do not need a cure for color blindness.'

    elif 2 <= num2 < 4:
        rep = 'Your color vision regarded as deficient. ' \
              'Special contact lenses and glasses may help people who are color blind tell the difference between ' \
              'colors. '

    else:
        rep = 'Your color vision regarded as badly worsened. ' \
              'You can use visual aids, apps, and other technology to help you live with color blindness. ' \
              'For example, you can use an app to take a photo with your phone or tablet and then tap on part of the ' \
              'photo to find out the color of that area. '

    doc = DocxTemplate("Report.docx")
    context = {'name': name, 'date': date, 'trueAns': num1, 'falseAns': num2, 'report': rep}
    doc.render(context)
    doc.save("Report_new.docx")  # make new report file in the same folder

# examples of game data for word file
name = 'David Israeli'
date = '01/01/2020'
num1 = 3
num2 = 1

wordInput(name, date, num1, num2)

######################## print word file
def readFile(fileName):
    doc = docx.Document(fileName)
    completedText = []
    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
    return '\n'.join(completedText)

# example:
# print(readFile('Report_new.docx')) #Need print!!!
#########################


listID = [name, date, num1, num2]  # example for game data
gamesList = [1, 2, 3, 4]  # example for list of game ID's


def menu(gameId, listOfGames):
    print('If you want list of games, enter "1"')
    print('If you want report of your game, enter "2"')
    ask = int(input('Enter here: '))

    if ask == 1:
        # print(listOfGames)  # print list of games ID
        for i in range(1, len(listOfGames)+1):
            print('Game ID: {}'.format(i))  # print ID of each game

        ask2 = int(input('Choose game that you want to have a report: '))
        wordInput(gameId[0], gameId[1], gameId[2], gameId[3])  # input data into report and make new report file
        print(readFile('Report_new.docx'))  # print new report file

    if ask == 2:
        wordInput(gameId[0], gameId[1], gameId[2], gameId[3])  # input data into report and make new report file
        print(readFile('Report_new.docx'))  # print new report file

# example of report menu:
# menu(listID, gamesList)  # print menu
