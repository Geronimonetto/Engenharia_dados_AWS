/*INTERVAL*/
/*Somando semanas*/
select (current_date + interval '25 weeks')
/*Somando Meses*/
select (current_date + interval '10 months')

/*Truncagem de datas utilizando DATE_TRUNC*/

select visit_page_date, count(*)
FROM sales.funnel 
GROUP BY visit_page_date
order by visit_page_date

/*DATE_TRUNC*/
select
	date_trunc('months', visit_page_date) as visita_por_mes,
	count(*)
from sales.funnel
group by visita_por_mes
order by visita_por_mes desc

/*Selecionando unidade de data*/
select '20230712'::date,
	extract('dow - day of week' from '20230712'::date )
	
select 
	extract('dow' from visit_page_date) as dia_semana,
	count(*) as contagem
from sales.funnel
group by dia_da_semana
order by dia_da_semana

/*Calculando diferença entre datas*/
select (current_date - '20211216')
select (current_date - '20211216')/7
select (current_date - '20211216')/30
select (current_date - '20211216')/365

select datediff('weeks', '20210601', current_date)
