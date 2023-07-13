select 
aut.nome as nome, 
aut.codautor as codautor, 
aut.nascimento as nascimento, 
count(publicacao) as quantidade 
from autor as aut left join livro on aut.codautor = livro.autor
group by codautor, nome, nascimento
order by nome asc



