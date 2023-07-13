SELECT COUNT(*) as quantidade, ed.nome as nome , en.estado as estado, en.cidade as cidade
from editora as ed  join livro on ed.codeditora = livro.editora
 JOIN endereco as en on ed.endereco = en.codendereco
group by nome, estado, cidade 
order by quantidade desc
limit 5;
	