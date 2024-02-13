-- displays the average temperature (Fahrenheit) by city ordered by temperature
select city, avg(value) as avg_temp from temperatures where month in
(7,8) group by city order by avg_temp desc limit 3;
