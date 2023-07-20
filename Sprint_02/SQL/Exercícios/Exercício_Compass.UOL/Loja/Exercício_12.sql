/*Apresente a query para listar código, nome e data de nascimento dos dependentes 
do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes 
no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.*/

select dep.cddep as cddep, dep.nmdep as nmdep, dep.dtnasc,SUM(vend.qtd * vend.vrunt) as valor_total_vendas
from tbdependente as dep left join tbvendedor as ven on dep.cdvdd = ven.cdvdd
LEFT join tbvendas as vend on ven.cdvdd = vend.cdvdd
WHERE vend.status = 'Concluído'
group by cddep, nmdep
ORDER by cddep DESC
limit 1
