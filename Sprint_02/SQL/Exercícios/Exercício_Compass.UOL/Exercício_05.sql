/*Apresente a query para listar o nome dos autores que publicaram livros 
através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, 
em ordem crescente. Não podem haver nomes repetidos em seu retorno.*/
SELECT DISTINCT aut.nome AS nome
FROM endereco AS en
JOIN editora AS edit ON en.codendereco = edit.endereco
JOIN livro ON livro.editora = edit.codeditora
JOIN autor AS aut ON aut.codautor = livro.autor
WHERE en.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL')
GROUP BY aut.nome
ORDER BY aut.nome ASC;