 /*Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, 
 nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.*/
 
SELECT COUNT(*) AS quantidade, ed.nome AS nome , en.estado AS estado, en.cidade AS cidade
FROM editora AS ed JOIN livro ON ed.codeditora = livro.editora
JOIN endereco AS en on ed.endereco = en.codendereco
GROUP BY nome, estado, cidade 
ORDER BY quantidade DESC
LIMIT 5;
	