from docxtpl import DocxTemplate

def wordInput(name, date, num1, num2):
    doc = DocxTemplate("Report.docx")
    context = {'name': name, 'date': date, 'trueAns': num1, 'falseAns': num2}
    doc.render(context)
    doc.save("Report_new.docx")

name='David Israeli'
date = '01/01/2020'
num1 = 3
num2 = 1

wordInput(name, date, num1, num2)
