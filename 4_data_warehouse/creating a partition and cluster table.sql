-- Creating a partition and cluster table
CREATE OR REPLACE TABLE green_taxi_2022.green_tripdata_2022_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM `green_taxi_2022.external_green_tripdata_2022`;
