import csv
from config import Config

def json_to_csv(json_data):
    csv_file = Config.get('csv_file_path')
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'value', 'latitude', 'station_id', 'channel_id', 'device_id', 'measurement_import_id', 'longitude', 'height', 'unit', 'devicetype_id', 'captured_at', 'sensor_id', 'location_name', 'original_id', 'user_id'])
        writer.writeheader()
        for entry in json_data:
            writer.writerow(entry)
