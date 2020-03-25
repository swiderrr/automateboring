import pyperclip, re

def strip(text, sub):
    spaceRegex = re.compile(r'(^\s+)(\s+$)')
    subRegex = re.compile(sub)
    
    if sub is '':
        text = spaceRegex.sub('', text)
        print(text)
    else:
        text = subRegex.sub('', text)
        print(text)

    

print('Wprowadź teskt do analizy.')
tekst = input()
print('Podaj co usunąć.')
zmiana = input()

strip(tekst, zmiana)
