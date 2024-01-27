SELECT 
date(lpep_pickup_datetime),
SUM(total_amount) AS Total,
CONCAT(zpu."Borough") AS "Pickup_Loc"
FROM 
green_trip_data g JOIN zones zpu
ON g."PULocationID" = zpu."LocationID"
WHERE date(lpep_pickup_datetime)='2019-09-18'
GROUP BY date(lpep_pickup_datetime),
CONCAT(zpu."Borough")
ORDER BY Total DESC;