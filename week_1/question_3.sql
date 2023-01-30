SELECT COUNT(1)
FROM green_taxi_trips
WHERE
	DATE(green_taxi_trips.lpep_pickup_datetime) = '2019-01-15'
	AND DATE(green_taxi_trips.lpep_dropoff_datetime) = '2019-01-15'