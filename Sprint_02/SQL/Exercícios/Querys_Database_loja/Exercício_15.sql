/*Apresente a query para listar os códigos das vendas identificadas como deletadas. 
Apresente o resultado em ordem crescente.*/

select cdven from tbvendas
WHERE deletado = true

