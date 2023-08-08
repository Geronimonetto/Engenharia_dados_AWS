mapeando = map(lambda x : x, range(1,10001))
filtrando = list(filter(lambda x : x <= 10000 and x %2 ==0 , mapeando))
ordem = sorted(filtrando,reverse=True)
five_numbers = ordem[:5]
print(five_numbers)
print(sum(five_numbers))
