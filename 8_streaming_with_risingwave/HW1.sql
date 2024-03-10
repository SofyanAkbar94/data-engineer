#Create Materialized View
CREATE MATERIALIZED VIEW trip_time_condition AS
SELECT
z1.zone AS pickup_zone,
z2.zone AS dropoff_zone,
AVG(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS avg_trip,
MIN(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS min_trip,
MAX(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))) AS max_trip
FROM
trip_data t
JOIN
taxi_zone z1
ON
t.pulocationid = z1.location_id
JOIN
taxi_zone z2
ON
t.dolocationid = z2.location_id
GROUP BY
z1.zone, z2.zone;

#Query highest average trip
SELECT
pickup_zone,
dropoff_zone,
avg_trip
FROM
trip_time_condition
ORDER BY
avg_trip DESC
LIMIT 10;
