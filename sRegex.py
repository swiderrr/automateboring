import re, os

#utworzenie regexa
print('Jakie wyrazenie znalezc w plikach?')

inputRegex = re.compile(raw_input())
#przelecenie przez wszystkie pliki
for file in os.listdir('C:\\Users\\Swider\\Desktop\\zadanie_teksty'):
    if file.endswith('.txt'):
        currentFile = open('C:\\Users\\Swider\\Desktop\\zadanie_teksty\\%s' % file, 'r').read().splitlines()
        for i, line in enumerate(currentFile):
            if inputRegex.search(line):
                print('Znaleziono wyszukiwana fraze w linijce ' + str(i+1) + ' w pliku ' + file)
    
        

