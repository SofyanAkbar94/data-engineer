-- Impact of partition
-- Scanning 1.12MB of data
SELECT DISTINCT(PULocationID)
FROM green_taxi_2022.green_tripdata_2022_partitioned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
