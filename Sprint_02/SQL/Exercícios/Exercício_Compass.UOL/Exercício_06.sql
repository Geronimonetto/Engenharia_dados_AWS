/*Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*/

select aut.codautor as codautor, aut.nome as nome, count(publicacao) as quantidade_publicacoes
from autor as aut join livro on aut.codautor = livro.autor
GROUP by codautor, nome
order by quantidade_publicacoes desc 
limit 1;


 
