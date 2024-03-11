#Query from Latest Pickup to know Busiest Zone
WITH LatestPickupTime AS (
  SELECT
    MAX(tpep_pickup_datetime) AS latest_pickup_time
  FROM
    trip_data
)

SELECT
  tz.Zone AS pickup_zone,
  COUNT(*) AS pickup_count
FROM
  trip_data trip
JOIN
  taxi_zone tz
ON
  trip.PULocationID = tz.location_id
JOIN
  LatestPickupTime lpt
ON
  trip.tpep_pickup_datetime BETWEEN (lpt.latest_pickup_time - INTERVAL '17 HOUR') AND lpt.latest_pickup_time
GROUP BY
  pickup_zone
ORDER BY
  pickup_count DESC
LIMIT 3;
