with open('oi.txt','r',encoding='utf-8') as teste:
    lista = []
    for v in teste:
        v = v.strip()
        v = v.replace('Stanley IRMÃO:','')
        v = v.split(']')
        lista.append(v)
    print(lista)
