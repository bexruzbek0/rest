birinchi = ['S001', 'S002', 'S003', 'S004']
ikkinchi = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
uchinchi = [85, 98, 89, 92]

d = []

for i in range(len(birinchi)):

    d.append({birinchi[i]: {ikkinchi[i]: uchinchi[i]}})

print (d)     

