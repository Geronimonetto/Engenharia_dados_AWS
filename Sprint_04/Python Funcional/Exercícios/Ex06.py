def maiores_que_media(conteudo: dict) -> list:
    """
    func: A função busca os produtos que estão acima da média dos valores
    return max_mean_products
    """
    mean_value = sum(conteudo.values()) / len(conteudo)
    max_mean_products = [(product, price) for product, price in conteudo.items() if price > mean_value]
    max_mean_products.sort(key=lambda x: x[1])
    return max_mean_products

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

finish = maiores_que_media(conteudo)
print(finish)