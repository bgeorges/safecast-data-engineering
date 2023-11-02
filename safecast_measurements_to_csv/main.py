from safecast_measurements import api_reader
from safecast_measurements import csv_writer


def main():
    # Fetch data using api_reader
    json_data = api_reader.fetch_data()

    # Process the data, e.g., convert it to CSV
    csv_writer.json_to_csv(json_data)
    print(json_data)


if __name__ == "__main__":
    main()