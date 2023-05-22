

# Unittest
python test_generate_random_values.py

# Generate random clinical data as specified in the file test_critera.tab

python criteria_runner.py --criteria test_critera.tab --outfile test.out -n 10

# Results are returned as a pandas DF, and you can add additional adjustments to the random values afterwards, such as adjusting length by age or gender, calculate BMI etc





