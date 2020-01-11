from docxtpl import DocxTemplate


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


name = 'David Israeli'
date = '01/01/2020'
num1 = 3
num2 = 1

wordInput(name, date, num1, num2)
