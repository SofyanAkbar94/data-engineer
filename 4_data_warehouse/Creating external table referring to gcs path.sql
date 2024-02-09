-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `green_taxi_2022.external_green_tripdata_2022`
OPTIONS (
  format = 'parquet',
  uris = ['gs://data_warehouse_de/green_tripdata_2022-*.parquet']
);
