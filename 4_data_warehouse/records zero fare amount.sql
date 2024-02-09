-- Records zero fare amount
SELECT count(*) as zero_fare
FROM `terraform-de-412207.green_taxi_2022.external_green_tripdata_2022` 
WHERE fare_amount=0;
