SELECT C.name, R.rentals_date
FROM customers as C, rentals as R
WHERE R.id_customers = C.id
AND EXTRACT(MONTH FROM R.rentals_date) = 9 
AND EXTRACT(YEAR FROM R.rentals_date) = 2016;
