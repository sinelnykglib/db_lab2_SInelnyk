SELECT TRIM(film_name), count(film_name) FROM dubs GROUP BY film_name

SELECT film_name, run_time from movie order by run_time

SELECT years, round(AVG(rate),2) from movie GROUP by years order by years