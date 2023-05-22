import argparse
import os
import criteria_mendelian_randomization
from criteria_mendelian_randomization import process_file
from criteria_mendelian_randomization import Criteria
import pandas as pd

parser = argparse.ArgumentParser(
    description = 'Generates random sequence of clinical and demographic features',
    usage = '%(prog)s [options] <infile> <outfile>')

#parser.add_argument('-n', '--iterations', default=10, dest='iter', action='store', required=True, help="Number of GSEA iterations")
parser.add_argument('-i','--criteria', dest='inp', action='store', required=True, help='Tab delimited criterion file', default = '')
parser.add_argument('-o','--outfile',dest='out', action='store', required=True, help='Name of fasta output file')
parser.add_argument('-n','--numbers',dest='nums', action='store', required=True, help='Number of random values to generate')

options = parser.parse_args()

# Check if input files exist
if not os.path.isfile(options.inp)==True:
    print("Cannot find input file ",options.inp)
    sys.exit(1)

if not os.path.isfile(options.inp)==True:
    print("Cannot find input file ",options.inp)
    sys.exit(1)


df = process_file(options.inp, options.nums)

print ("FIRST")
print (df)

# Adjust values for Height and Weight columns so that women are shorter and lighter
#df.loc[df['Gender'] == 'female', ['Height', 'Weight']] *= 0.9
#df.loc[df.loc['Gender'] == 'female', ['Height', 'Weight']] *= 0.9
#print (df.loc['Gender' == 'female'])

# Adjust values in the "Height" row based on "Gender" row
if df.loc['Gender'].str.contains('female').any():
    df.loc['Height'] *= 0.9


# Adjust values in the "Weight" row based on "Gender" row
if df.loc['Gender'].str.contains('female').any():
    df.loc['Weight'] *= 0.9


# Calculate BMI and create a new row
#df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)
df.loc['BMI'] = df.loc['Weight']/  ((df.loc['Height'] / 100) ** 2)


print()
print ("ADJUSTED")
print (df)


 
