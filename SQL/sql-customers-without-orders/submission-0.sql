-- Write your query below

with ct as (select cus.name,o.id from 
customers  as cus
left join orders o
on o.customer_id =cus.id
where o.id is Null)

select name from ct
