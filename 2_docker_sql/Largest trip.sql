SELECT date(lpep_pickup_datetime), MAX(trip_distance) as Max
FROM green_trip_data
GROUP BY date(lpep_pickup_datetime)
ORDER BY Max DESC;