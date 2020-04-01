import os, re

#Odczytanie pliku
madText = open('C:\\Users\\Swider\\Desktop\\tekst.txt', 'r')
tekst = re.split(r'(\s|\.)', madText.read())
print(tekst)

#tekst = madText.read().split()
slowaKlucze = ['przymiotnik', 'rzeczownik', 'czasownik']
#Wyszukiwanie jednego z czterech słów
madText = open('C:\\Users\\Swider\\Desktop\\tekst.txt', 'w')
for i, word in enumerate(tekst):
    if word.lower() in slowaKlucze:
        print('Podaj ' + word.lower() + ':\n')
        tekst[i] = input()

#Zapisanie pliku
madText.write(''.join(tekst))
madText.close()
print(tekst)
