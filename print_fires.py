import argparse
from my_utils import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--country",
                        type=str,
                        help="Name of the country",
                        required=True)

    parser.add_argument("--country_column",
                        type=int,
                        help="Column index containing country names",
                        required=True)

    parser.add_argument("--fires_column",
                        type=int,
                        help="Column index containing fire data",
                        default=1,
                        required=False)

    parser.add_argument("--file_name",
                        type=str,
                        help="Name of file",
                        required=True)

    args = parser.parse_args()

    # Pulls data for a specific country (only successful for integer-filled columns)
    fires = get_column(
        args.file_name, 
        args.country_column, 
        args.country, 
        args.fires_column
    )

    print(fires)

if __name__ == "__main__":
    main()