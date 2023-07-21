/*Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), 
em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/
select 
aut.nome as nome, 
aut.codautor as codautor, 
aut.nascimento as nascimento, 
count(publicacao) as quantidade 
from autor as aut left join livro on aut.codautor = livro.autor
group by codautor, nome, nascimento
order by nome asc



