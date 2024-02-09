-- Create a partitioned table from external table
CREATE OR REPLACE TABLE green_taxi_2022.green_tripdata_2022_partitioned
PARTITION BY
  DATE(lpep_pickup_datetime) AS
SELECT * FROM green_taxi_2022.external_green_tripdata_2022;
