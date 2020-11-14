import re, os, shutil

def sortName(folder, prefix):

    prefix = input()
    folder = os.path.abspath('H:\Programowanie\Python\Zadania Python\PREFIX')
    prefixRegex = re.compile(r'(^{}\d\d\d(.txt)$)'.format(prefix))
    gaps = []
    fills = []
    for filename in os.listdir(folder):
        if re.search(prefixRegex, filename):
            gaps.append(filename)
    gaps.sort()
    for i in range(len(gaps)):
        fills.append('{}{:0>3}.txt'.format(prefix, i+1))
        shutil.move(f'{folder}\\{gaps[i]}', f'{folder}\\{fills[i]}')



sortName('H:\Programowanie\Python\Zadania Python\PREFIX', 'spam')
    
        
        
    
