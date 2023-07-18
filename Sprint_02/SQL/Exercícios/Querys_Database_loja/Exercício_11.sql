/*Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, 
nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.*/

select tbvendas.cdcli, tbvendas.nmcli, SUM(tbvendas.qtd * tbvendas.vrunt) as gasto 
from tbvendas 
where tbvendas.status = 'Concluído'
group by tbvendas.cdcli,tbvendas.nmcli
order by gasto DESC
limit 1