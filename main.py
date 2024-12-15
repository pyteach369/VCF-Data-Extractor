"""This File will extract all phone numbers from a .vsf file."""
# imports
import re
import quopri

# Getting path of the vcf file:
path = input('Drag&Drop: ')

# Reading the vcf file:
with open(path, 'r') as f:
    text = f.read()

# Regex pattern that matches name and phone number :
# FIRS GROUP is the name and the SECOND GROUP is the phone number:
pattern = r'((?<=FN:).+|(?<=FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:).+\n?[^T\s]+\n?[^T\s]+)(?:\nTEL;CELL:)((?<=CELL:).+)'

# Final result:
new_other = []
new_main = []

# Get all the Matches:
for i in re.findall(pattern, text, re.M):
    # Check if NAME needed to be decode or not:
    if i[0][0] == '=':
        p = quopri.decodestring(i[0])
        p = p.decode('utf-8')
        new_other.append((p, i[1]))
    else:
        new_main.append(i)

with open('result.txt', 'w', encoding='utf-8') as f:
    for i in new_other:
        f.write(f'{i[1]}  -> {i[0]}\n')

    for i in new_main:
        f.write(f'{i[1]}  -> {i[0]}\n')
