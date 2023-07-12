/*Análise de recorrência dos leads, calcule o volume de visitas por dia ao site separado por 1ª visita e demais visitas*/
with primeira_data as (
	select 
	customer_id,min(visit_page_date) as menordata
	from sales.funnel
	group by customer_id
)

select
	fun.visit_page_date,
	(fun.visit_page_date <> primeira_data.menordata) as lead_recorrente,
	count(*)
from sales.funnel as fun
left join primeira_data  
	on fun.customer_id = primeira_data.customer_id
group by fun.visit_page_date, lead_recorrente
order by fun.visit_page_date DESC, lead_recorrente

/*Análise do preço versus o preço médio
Calcule para cada visita ao site, quanto o preço do 
veículo visitado pelo cliente estava acima ou abaixo do 
preço média dos veículos daquela marca
*/

with preco_medio as (
		select 
			brand, avg(price) as preco_medio_da_marca
		from sales.products
		group by brand
)
select
	fun.visit_id,
	fun.visit_page_date,
	pro.brand,
	((pro.price* (1+fun.discount))) as preco_final,
	preco_medio.preco_medio_da_marca,
	((pro.price * (1+fun.discount)) - preco_medio.preco_medio_da_marca)
from sales.funnel as fun
left join sales.products as pro
	on fun.product_id = pro.product_id
left join preco_medio
	on pro.brand = preco_medio.brand



