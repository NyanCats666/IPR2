import gzip
import re

with gzip.open('csv_example.csv.gz', 'rb') as f:
    logs = f.read()
    print(logs)