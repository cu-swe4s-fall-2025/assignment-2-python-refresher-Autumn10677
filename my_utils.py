import numpy as np

def get_column(file_name, query_column, query_value, result_column=1):

    results = np.array([])

    f = open(file_name, "r")
    for l in f:
        A = l.rstrip().split(",")
        
        if A[query_column]==query_value:
            results = np.append(results, A[result_column])

    f.close()

    return results
