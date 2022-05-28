import argparse
import urllib.request

TRIP_DATA_BASE_URL = "https://nyc-tlc.s3.amazonaws.com/trip+data"
DATASET_NAME = "green_tripdata"


def download_file(file_identifier: str, output_path: str):
    file_url = f"{TRIP_DATA_BASE_URL}/{DATASET_NAME}_{file_identifier}.parquet"
    print(file_url)

    response = urllib.request.urlopen(file_url)  # nosec B310
    f = open(f"{output_path}/{DATASET_NAME}_{file_identifier}.parquet", "wb")
    f.write(response.read())
    f.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file_identifier",
        required=True,
        help="the <year-month>(yyyy-mm) combination for interested parquet",
    )

    parser.add_argument(
        "--raw_data_path",
        default="./artifacts/data/raw",
        help="folder path for saving downloaded raw file",
    )

    args = parser.parse_args()

    download_file(args.file_identifier, args.raw_data_path)
