/* (Exemplo 1) Agrupamento de dados com CASE WHEN
Calcule o nº de clientes que ganham abaixo de 5k, entre 5k e 10k, entre 10k e
15k e acima de 15k*/

with faixa_salario as (
	select 
		income,
		case 
			when income <= 5000 then 'Abaixo de 5k'
			when income >= 5000 and income < 10000 then 'Entre 5k e 10k'
			when income >= 10000 and income < 15000 then 'Entre 10k e 15k'
			else 'Acima de 15k'
			end as salaries
	from sales.customers
)

select salaries,
count(*)
from faixa_salario
group by salaries


/*(Exemplo 2) Tratamento de dados nulos com COALESCE
Crie uma coluna chamada populacao_ajustada na tabela temp_tables.regions e
preencha com os dados da coluna population, mas caso esse campo estiver nulo, 
preencha com a população média (geral) das cidades do Brasil*/

/*usando case WHEN para substituir campos nulos*/
select *,
	case 
		when population is not null then population
		else (select avg(population) from temp_tables.regions)
		end as populacao_media
from temp_tables.regions;

/*Usando coalesce para substituir campos nulos*/
select 
	*,
	coalesce(population,(select avg(population) from temp_tables.regions)) as populacao_ajustada
from temp_tables.regions

/*O coalesce verifica a primeira coluna caso ela esteja nula, verifica a segunda, 
podendo ter uma lista*/