import os, re, shutil

znakRegex = re.compile(r'([-a-zA-Z.123456789])')
zeroRegex = re.compile(r'(0)')

for folderName, subfolders, filenames in os.walk('H:\Programowanie\Python'):
    for nowaNazwa in filenames:
        staraNazwa = nowaNazwa
        if zeroRegex.search(nowaNazwa) == None:
            continue
        match = znakRegex.findall(nowaNazwa)
        print(match)
        nowaNazwa = ''.join(match)
        print(nowaNazwa)
        
        nowaSciezka = folderName + '\\' + nowaNazwa
        staraSciezka = folderName + '\\' + staraNazwa
        shutil.move(staraSciezka, nowaSciezka)
    
 
        
