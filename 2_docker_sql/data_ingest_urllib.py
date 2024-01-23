import urllib.request
import csv
import codecs

url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
file_path = 'C:/VULCAN_HOME/git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/output.csv'

urllib.request.urlretrieve(url, file_path)

with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)