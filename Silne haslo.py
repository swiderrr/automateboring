import re

print('Wprowadz haslo: ')
haslo = input()

charRegex = re.compile(r'(\W+|\-)')
bcaseRegex = re.compile(r'[A-Z+]')
lcaseRegex = re.compile(r'[a-z+]')
digitRegex = re.compile(r'[0-9+]')

#while (charRegex.search(haslo), bcaseRegex.search(haslo), lcaseRegex.search(haslo), digitRegex.search(haslo)) != None: #and (len(haslo) >= 8):
while len(haslo) < 7 or (lcaseRegex.search(haslo) and bcaseRegex.search(haslo) and charRegex.search(haslo) and digitRegex.search(haslo)) is None:
    print('Hasło jest za słabe. Wprowadź nowe: ')
    haslo = input()


print('Bardzo dobre hasło!')
