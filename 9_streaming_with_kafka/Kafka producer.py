import pandas as pd
from kafka import KafkaProducer
import time 
from datetime import datetime

# Record the start time
start_time = time.time()

# Create a KafkaProducer instance
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Define the topic name
topic = 'green-trips'

# Define the data types for each column
dtype_dict = {
    'PULocationID': 'Int64',  # Use 'Int64' instead of 'int' to support NA values
    'DOLocationID': 'Int64',  # Use 'Int64' instead of 'int' to support NA values
    'passenger_count': 'Int64',  # Use 'Int64' instead of 'int' to support NA values
    'trip_distance': 'float',
    'tip_amount': 'float'
}

# Define the columns you want to keep
columns_to_keep = [
    'lpep_pickup_datetime',
    'lpep_dropoff_datetime',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'tip_amount'
]

# Read the CSV file into a DataFrame, specifying the dtype parameter
df_green = pd.read_csv('C:/Users/msofy/Downloads/Kafka_Streams/green_tripdata_2019-10/green_tripdata_2019-10.csv', usecols=columns_to_keep, dtype=dtype_dict, na_values=[''])

# Fill missing values in integer columns with zeros
int_columns = ['PULocationID', 'DOLocationID', 'passenger_count']
df_green[int_columns] = df_green[int_columns].fillna(0).astype('Int64')

# Convert timestamp columns to strings
df_green['lpep_pickup_datetime'] = df_green['lpep_pickup_datetime'].astype(str)
df_green['lpep_dropoff_datetime'] = df_green['lpep_dropoff_datetime'].astype(str)

# Iterate over each row of the DataFrame
for row in df_green.itertuples(index=False):
    # Convert timestamp columns to ISO 8601 format
    row_dict = {col: getattr(row, col) for col in row._fields}
    row_dict['lpep_pickup_datetime'] = datetime.fromisoformat(row_dict['lpep_pickup_datetime']).isoformat()
    row_dict['lpep_dropoff_datetime'] = datetime.fromisoformat(row_dict['lpep_dropoff_datetime']).isoformat()
    
    # Convert the dictionary to JSON and encode as bytes
    message = pd.Series(row_dict).to_json().encode('utf-8')
    
    # Send the message to the Kafka topic
    producer.send(topic, value=message)
    
# Close the producer
producer.close()

# Record the end time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

# Print the execution time
print(f"Script execution completed in {execution_time:.2f} seconds.")
