/*Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/

select cdpro, nmcanalvendas, nmpro, SUM(qtd) as quantidade_vendas
from tbvendas as vend
WHERE vend.status = 'Concluído'
group by cdpro,nmpro,nmcanalvendas
order by quantidade_vendas

