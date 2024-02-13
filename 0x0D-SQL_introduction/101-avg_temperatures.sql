-- displays the average temperature (Fahrenheit) by city ordered by temperature
select city, avg(value) as avg_temp from temperatures group by city order by
avg_temp desc;
