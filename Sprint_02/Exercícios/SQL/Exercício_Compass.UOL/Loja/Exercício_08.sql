/*Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.*/
select ven.cdvdd,ven.nmvdd
from tbvendedor as ven
left join tbvendas on 
	ven.cdvdd = tbvendas.cdvdd
GROUP by ven.cdvdd
order by count(tbvendas.cdvdd) desc
limit 1