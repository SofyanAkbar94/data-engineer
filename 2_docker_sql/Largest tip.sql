SELECT 
date(lpep_dropoff_datetime),
MAX(tip_amount) AS Largest_Tip,
CONCAT(zpu."Zone") AS "PickUp_Loc",
CONCAT(zdo."Zone") AS "DropOff_Loc"
FROM 
green_trip_data g JOIN zones zpu
ON g."PULocationID" = zpu."LocationID"
JOIN zones zdo
ON g."DOLocationID" = zdo."LocationID"
WHERE zpu."Zone"='Astoria'
GROUP BY date(lpep_dropoff_datetime),
CONCAT(zpu."Zone"),
CONCAT(zdo."Zone")
ORDER BY Largest_Tip DESC;