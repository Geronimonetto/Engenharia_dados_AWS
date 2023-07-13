/*Apresente a query para listar o nome dos autores com nenhuma publicação. 
Apresentá-los em ordem crescente.*/
SELECT aut.nome 
FROM autor AS aut 
left JOIN livro ON aut.codautor = livro.autor
GROUP BY aut.nome
HAVING COUNT(publicacao) < 1
ORDER BY aut.nome;





