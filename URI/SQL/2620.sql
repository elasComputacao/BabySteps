SELECT c.name, o.id
FROM customers as c, orders as o
WHERE o.id_customers = c.id
AND EXTRACT(YEAR FROM o.orders_date) = 2016
AND EXTRACT(MONTH FROM o.orders_date) <= 6;
