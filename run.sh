echo "Working example:"
python ./print_fires.py \
    --country "Afghanistan" \
    --country_column 0 \
    --fires_column 1 \
    --file_name "Agrofood_co2_emission.csv"

echo ""
echo "Example with wrong filename:"
python ./print_fires.py \
    --country "Afghanistan" \
    --country_column 0 \
    --fires_column 1 \
    --file_name "Agrofood_co2_emission.txt"

echo ""
echo "Example with invalid return column:"
python ./print_fires.py \
    --country "Afghanistan" \
    --country_column 0 \
    --fires_column 2 \
    --file_name "Agrofood_co2_emission.csv"