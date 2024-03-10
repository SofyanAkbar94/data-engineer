WITH trip AS ( SELECT MAX(tpep_dropoff_datetime) AS latest_dropoff_time FROM trip_data ) 

SELECT taxi_zone.Zone as taxi_zone, latest_dropoff_time FROM trip, 

trip_data JOIN taxi_zone 

ON trip_data.DOLocationID = taxi_zone.location_id 

WHERE trip_data.tpep_dropoff_datetime = trip.latest_dropoff_time;
