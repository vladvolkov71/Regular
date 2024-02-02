import re
import csv
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    cl = list(rows)
    fields = cl[0]
    del (cl[0])


def phone(string):
    pat = r'(\+7|8)*\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d\d)[\s-]*(\d\d)\s*\(*(доб\.)*\)*\s*(\d{4})*\)*'
    return re.sub(pat, r'+7(\2)\3-\4-\5 \6\7', string)


def name(i0, i1, i2):
    ln, fn, sn = '', '', ''
    s0 = re.findall(r'\b\w+\b', f'{i0} {i1} {i2}')
    if len(s0) == 3:
        ln, fn, sn = (s0[0], s0[1], s0[2])
    elif len(s0) == 2:
        ln, fn = (s0[0], s0[1])
    else:
        ln = s0[0]
    return ln, fn, sn


new_cl = []

for i in cl:
    lastname, firstname, surname = name(i[0], i[1], i[2])
    new_cl.append(
        {'lastname': lastname, 'firstname': firstname, 'surname': surname, 'organization': i[3], 'position': i[4],
         'phone': phone(i[5]), 'email': i[6]})
# Объединение одинаковых записей
for i in new_cl:
    for j in new_cl:
        if i == j:
            continue
        if i['lastname'] == j['lastname'] and i['firstname'] == j['firstname']:
            s = {}
            for k, v in i.items():
                if v == '':
                    i[k] = j[k]
            new_cl.remove(j)

pprint(new_cl, width=120, sort_dicts=False)

with open('phonebook.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields, delimiter=',')
    writer.writeheader()
    for row in new_cl:
        writer.writerow(row)
