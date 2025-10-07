import sys
import argparse
import my_utils


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

    # Error handling for invalid operation input
    if args.operation.lower() not in ["default", "mean", "median", "std"]:
        print(
            f"Operation '{args.operation}' not recognized. \
            Please use 'mean', 'median', 'std'"
        )
        sys.exit(1)

    # Pulls integer data for a specific country
    fires = my_utils.get_column(
        args.file_name, args.country_column, args.country, args.fires_column
    )

    # Performs requested operation
    if args.operation.lower() == "mean":
        fires = my_utils.mean(fires)
    elif args.operation.lower() == "median":
        fires = my_utils.median(fires)
    elif args.operation.lower() == "std":
        fires = my_utils.standard_deviation(fires)

    print(fires)


if __name__ == "__main__":
    main()
