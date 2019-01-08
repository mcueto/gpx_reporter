"""reporter module."""
import os
from utils import (
    open_gpx_file,
    gpx_to_json,
)


def main():
    files_folder = 'files'
    file_list = os.listdir(files_folder)

    for filename in file_list:
        if filename.endswith(".gpx"):
            # Open file
            filepath = '{folder}/{filename}'.format(
                folder=files_folder,
                filename=filename
            )

            gpx = open_gpx_file(filepath)

            # Read file to json
            json = gpx_to_json(gpx)

            # Print in a format(markdown stylish)
            print(json)


if __name__ == "__main__":
    main()
