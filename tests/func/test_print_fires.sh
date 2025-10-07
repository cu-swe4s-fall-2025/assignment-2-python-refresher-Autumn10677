test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Basic functionality tests
run retrieval_test python src/print_fires.py --country "Afghanistan" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv"
assert_exit_code 0
assert_in_stdout "[1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]"

run valid_mean_test python src/print_fires.py --country "Afghanistan" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv" --operation "mean"
assert_exit_code 0
assert_in_stdout "2005.0"

run valid_median_test python src/print_fires.py --country "Algeria" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv" --operation "median"
assert_exit_code 0
assert_in_stdout "2005"

run valid_std_test python src/print_fires.py --country "Albania" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv" --operation "std"
assert_exit_code 0
assert_in_stdout "8.94427190999916"

run empty_return_test python src/print_fires.py --country "Fake Country" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv"
assert_exit_code 0
assert_in_stdout "[]"

# Error handling tests
run non_integer_test python src/print_fires.py --country "Afghanistan" --country_column 0 --fires_column 2 --file_name "src/subset_data.csv"
assert_exit_code 1

run invalid_file_test python src/print_fires.py --country "Afghanistan" --country_column 0 --fires_column 1 --file_name "src/fake_dataset.csv"
assert_exit_code 1

run invalid_operation_test python src/print_fires.py --country "Afghanistan" --country_column 0 --fires_column 1 --file_name "src/subset_data.csv" --operation "invalid_operation"
assert_exit_code 1

run invalid_mean_test python src/print_fires.py --country "Fake Country" --country_column 0 --fires_column 2 --file_name "src/subset_data.csv" --operation "mean"
assert_exit_code 1

run invalid_median_test python src/print_fires.py --country "Fake Country" --country_column 0 --fires_column 2 --file_name "src/subset_data.csv" --operation "median"
assert_exit_code 1

run invalid_std_test python src/print_fires.py --country "Fake Country" --country_column 0 --fires_column 2 --file_name "src/subset_data.csv" --operation "std"
assert_exit_code 1