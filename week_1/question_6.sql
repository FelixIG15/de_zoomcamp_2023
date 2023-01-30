SELECT tips_zone_t.*
FROM(
	SELECT g.tip_amount, pu_z."Zone" AS pu_zone, do_z."Zone" AS do_zone
	FROM green_taxi_trips g
	LEFT JOIN taxi_zone_lookup pu_z
		ON g."PULocationID" = pu_z."LocationID"
	LEFT JOIN taxi_zone_lookup do_z
		ON g."DOLocationID" = do_z."LocationID"
) tips_zone_t
WHERE tips_zone_t.pu_zone = 'Astoria'
ORDER BY tips_zone_t.tip_amount DESC