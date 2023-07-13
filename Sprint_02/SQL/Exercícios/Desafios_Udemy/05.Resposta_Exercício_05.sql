/*Exercício 01*/
with visita_cliente as (
		select
		customer_id,count(*) as visitas_feitas 
		from sales.funnel 
		group by customer_id
)
select
	cus.*,
	visitas_feitas
from sales.customers as cus
left join visita_cliente as cli_vi 
	on cus.customer_id = cli_vi.customer_id




