import csv
from config import Config

def json_to_csv(json_data):
    csv_file = Config.get('csv_file_path')
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "id", "value"])
        writer.writeheader()
        for entry in json_data:
            writer.writerow(entry)
