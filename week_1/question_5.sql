SELECT  green_taxi_trips.passenger_count, COUNT(1) AS count
FROM    green_taxi_trips
WHERE 	DATE(green_taxi_trips.lpep_pickup_datetime) = '2019-01-01'
GROUP BY green_taxi_trips.passenger_count