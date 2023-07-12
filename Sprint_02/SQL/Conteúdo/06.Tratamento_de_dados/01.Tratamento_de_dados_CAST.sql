/*Conversão de texto em data*/
select '2023-07-11'::date - '2021-02-01'::date

select nome_coluna::date - transforma todos os dados da coluna em data
from nome_tabela

/*Convertendo texto em número*/
select '100'::numeric - '10'::numeric

/*Convertendo um numero em texto*/
select replace(112122::text,'1','A')

/*Converter texto em data*/
select cast('2021-01-10' as date) - cast('2021-02-01' as date) 
o cast() - o parâmetro do apelido é a conversão