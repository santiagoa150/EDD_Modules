data = {
    'pdd': set(),
    'pdi': set(),
    'pdc': set(),
}
while True:
    line = input()
    if line == "#":
        break

    ID, pd = line.split()
    data[pd].add(ID)

all_data = data['pdd'] & data['pdi'] & data['pdc']
data['pdd'] = data['pdd'] - all_data
data['pdi'] = data['pdi'] - all_data
data['pdc'] = data['pdc'] - all_data

pdd_pdi = data['pdd'] & data['pdi']
data['pdd'] = data['pdd'] - pdd_pdi
data['pdi'] = data['pdi'] - pdd_pdi

pdd_pdc = data['pdd'] & data['pdc']
data['pdd'] = data['pdd'] - pdd_pdc
data['pdc'] = data['pdc'] - pdd_pdc

pdi_pdc = data['pdi'] & data['pdc']
data['pdi'] = data['pdi'] - pdi_pdc
data['pdc'] = data['pdc'] - pdi_pdc

print(len(data['pdd'] | data['pdi'] | data['pdc']), len(pdd_pdi | pdd_pdc | pdi_pdc), len(all_data))
