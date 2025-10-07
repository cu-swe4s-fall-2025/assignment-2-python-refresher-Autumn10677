import argparse
from my_utils import *


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--country",
        type=str,
        help="Name of the country",
        required=True,
    )

    parser.add_argument(
        "--country_column",
        type=int,
        help="Column index containing country names",
        required=True,
    )

    parser.add_argument(
        "--fires_column",
        type=int,
        help="Column index containing fire data",
        default=1,
        required=False,
    )

    parser.add_argument(
        "--file_name",
        type=str,
        help="Name of file",
        required=True,
    )

    parser.add_argument(
        "--operation",
        type=str,
        help="Statistical operation to perform (mean, median, std)",
        default="default",
        required=False,
    )

    args = parser.parse_args()

    # Error handling for invalid operation input (converts to lowercase for flexibility)
    if args.operation.lower() not in ["default", "mean", "median", "std"]:
        print(
            f"Operation '{args.operation}' not recognized. Please use 'mean', 'median', 'std'"
        )
        sys.exit(1)

    # Pulls data for a specific country (only successful for integer-filled columns)
    fires = get_column(
        args.file_name, args.country_column, args.country, args.fires_column
    )

    # Performs requested operation
    if args.operation.lower() == "mean":
        fires = mean(fires)
    elif args.operation.lower() == "median":
        fires = median(fires)
    elif args.operation.lower() == "std":
        fires = standard_deviation(fires)

    print(fires)


if __name__ == "__main__":
    main()
