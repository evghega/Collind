from docxtpl import DocxTemplate


def wordInput(date, title, fname, sname):
    doc = DocxTemplate("Example.docx")
    context = {'date': date, 'title': title, 'firstName': fname, 'secondName': sname}
    doc.render(context)
    doc.save("Example_new.docx")


date = '01/01/2020'
title = 'Example sheet'
fname = 'David Israeli'
sname = 'Shlomo Koen'

wordInput(date, title, fname, sname)
