/*Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.*/

SELECT cdpro, nmpro from tbvendas 
WHERE dtven BETWEEN '2014-02-03' and '2018-02-02' and tbvendas.status = 'Concluído'
group by cdpro, nmpro
ORDER by nmpro
limit 1