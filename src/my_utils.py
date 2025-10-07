import sys


def get_column(file_name, query_column, query_value, result_column=1):
    """
    Retrieves integer data from a specified column for
    rows where another column matches a given query value.

    Parameters:
    -----------
    file_name : str
        Name of the file to load data from.
    query_column :: int
        Column index used for querying data.
    query_value : str
        Value to filter by in the query column.
    result_column : int
        Column index containing integer data.

    Returns:
    --------
    results : list of ints
        List of integers from the result column
    """

    results = []

    try:
        f = open(file_name, "r")

        for l in f:
            entry = l.rstrip().split(",")

            if entry[query_column] == query_value:
                try:
                    results.append(int(entry[result_column]))

                # Error handling for non-integer values (this includes floats)
                except ValueError:
                    print(
                        f"Non-integer value `{entry[result_column]}` found in return column."
                    )
                    f.close()
                    sys.exit(1)

        f.close()

    # Error handling if the provided file does not exist
    except FileNotFoundError:
        print(f"Filename '{file_name}' could not be found.")
        sys.exit(1)

    return results


def mean(array):
    """
    Calculates the mean of a list of numbers.

    Parameters:
    -----------
    array :: list of ints
        List of numbers to calculate the mean of.

    Returns:
    --------
    mean :: float
        The mean of the list of numbers.
    """

    if not array:
        raise ValueError("mean() arg is an empty array")
    return sum(array) / len(array)


def median(array):
    """
    Calculates the median of a list of numbers.

    Parameters:
    -----------
    array :: list of ints
        List of numbers to calculate the median of.

    Returns:
    --------
    median :: int or float
        The median of the list of numbers.
    """

    if not array:
        raise ValueError("median() arg is an empty array")
    sorted_array = sorted(array)
    n = len(sorted_array)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_array[mid - 1] + sorted_array[mid]) / 2
    return sorted_array[mid]


def standard_deviation(array):
    """
    Calculates the standard deviation of a list of numbers.

    Parameters:
    -----------
    array :: list of ints
        List of numbers to calculate the standard deviation of.

    Returns:
    --------
    standard_deviation :: float
        The standard deviation of the list of numbers.
    """

    if not array:
        raise ValueError("standard_deviation() arg is an empty array")
    avg = mean(array)
    variance = sum((x - avg) ** 2 for x in array) / len(array)
    return variance**0.5
