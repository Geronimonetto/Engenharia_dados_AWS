with open('oi.txt','r',encoding='utf-8') as teste:
    lista = []
    for v in teste:
        v = v.strip()
        v = v.replace('Stanley IRMÃO:','')
        v = v.replace('mamão','Mamão').replace('Mamao','Mamão').replace('formosa','Formosa').replace('mamao','Mamão').replace('esponhol','Espanhol').replace('melao','Melão')
        v = v.split(']')
        if len(v) ==2:
            lista.append(v[1])
        elif 'kl' in v or 'un' in v:
            lista.append(v[1])

for valor in lista:
    print(valor)
