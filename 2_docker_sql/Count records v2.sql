SELECT count(*)
FROM green_trip_data
WHERE date(lpep_pickup_datetime)='2019-09-18'
AND date(lpep_dropoff_datetime)='2019-09-18';