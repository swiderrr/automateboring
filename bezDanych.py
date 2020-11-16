import sys, docx, re


path = str(sys.argv[1])
town = str(sys.argv[2])
town = 'Radwanki'
doc = docx.Document(path)

def tableReplace():
    table = doc.tables
    tableText = []
    print(table)
    for t in range(len(table)):
        for row in (table[t].rows):
            for cell in row.cells:
                paragraphs = cell.paragraphs
                for paragraph in paragraphs:
                    if town in paragraph.text:
                        for run in paragraph.runs:
                            if town in run.text:
                                print(run)
                                text = run.text.replace(town, '')
                                run.text = text

def textReplace():
    idRegex = re.compile(r'(\d{6}_\d{1,2}.\d{4}.)')
    for paragraph in doc.paragraphs:
        if idRegex.search(paragraph.text):
            for run in paragraph.runs:
                if idRegex.search(run.text):
                    match = idRegex.search(run.text).group(0)
                    text = run.text.replace(match, '')
                    run.text = text

tableReplace()
textReplace()
doc.save('H:\\Programowanie\\Python\\PROBA.docx')
    



     
    
