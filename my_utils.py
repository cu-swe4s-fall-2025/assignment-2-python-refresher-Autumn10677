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
            A = l.rstrip().split(",")
        
            if A[query_column]==query_value:
                try:
                    results.append(int(A[result_column]))

                # Error handling for non-integer values (this includes floats)
                except ValueError:
                    print(f"Non-integer value `{A[result_column]}` found in return column.")
                    f.close()
                    sys.exit(1)

        f.close()

    # Error handling if the provided file does not exist
    except FileNotFoundError:
        print(f"Filename '{file_name}' could not be found.")
        sys.exit(1)

    return results
