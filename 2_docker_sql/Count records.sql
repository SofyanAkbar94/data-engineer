SELECT 
   COUNT(lpep_pickup_datetime),
   COUNT(lpep_dropoff_datetime)
FROM 
   green_trip_data g
WHERE
   lpep_pickup_datetime @@ to_tsquery('2019-09-18') AND lpep_dropoff_datetime @@ to_tsquery('2019-09-18');