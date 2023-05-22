#!/usr/bin/env python3

import argparse
import os
import random
import numpy as np
import re
import pandas as pd




def process_file(inp,n):
    columns = list(range(int(n)))
    df = pd.DataFrame(columns=columns)
    #print(df)

    with open(inp, "r") as file:
        lines = file.readlines()
        # Remove the first line
        lines = lines[1:]

        for line in lines:
            print ()
            print (line)
            columns = line.strip().split('\t')
            column_3 = columns[2]
            #print ("Third ",column_3)	
            column_4=columns[3].lower()

          # Process line based on column 3 value
            if contains_dash(columns[1]):
                # Code to process for a float value
                start, end = columns[1].split('-')
                start = int(start)
                end = int(end)
                value_range = range(start, end + 1)
                #print("Range:", value_range)
                criteria_obj = Criteria([start,end],int(n), column_4) 
                randval = criteria_obj.generate_random_values()
                #print (randval)
                df.loc[columns[4]] = randval
                #print(df)

            elif is_float(column_3):
                # Code to process for a float value
                float_value = float(column_3)
                #print("Float value:", float_value)
                generate_random_values

            else:
                # Code to process for a categorical value
                categorical_values = columns[1].split(',')
                #print("Categorical value:", categorical_values)
                criteria_obj = Catval(categorical_values,int(n),float(columns[3]))
                randval = criteria_obj.generate_random_catval()
                #print (randval)
                df.loc[columns[4]] = randval
                #print(df)

    return df   


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def contains_dash(variable):
    pattern = r".*-.*"
    match = re.match(pattern, variable)
    if match:
        return True
    else:
        return False



class Catval:
    def __init__(self, r, n,prop):
        self.r = r
        self.n = n
        self.prop=prop

    def generate_random_catval(self):
        # Calculate the number of values for each category based on the proportion
        num_category1 = int(self.n * self.prop)
        num_category2 = self.n - num_category1
        #print("CATS",num_category1, num_category2)
        # Create a list of categories based on the self.r list
        categories=[]
        categories = ([self.r[0]] * num_category1)
        categories = categories + ([self.r[1]] * num_category2)
        #print (categories)
        # Shuffle the categories randomly
        random.shuffle(categories)

        return categories

'''
    def generate_random_catval(self):
        categories = self.r
        random_catval = [random.choice(categories) for _ in range(self.n)]
        return random_catval
'''


class Criteria:
    def __init__(self, r, n, distribution_type):
        self.r = r
        self.n = int(n)
        self.distribution_type = distribution_type  

    def generate_random_values(self):
        # Initialize the list of random values
        randval = []
        #print (self.r, self.distribution_type, self.n)
        if self.distribution_type == "uniform":
            # Uniform distribution
            for _ in range(self.n):
                value = random.uniform(self.r[0], self.r[1])
                randval.append(value)
        elif self.distribution_type == "normal":
            # Normal distribution
            for _ in range(self.n):
                value = np.random.normal((self.r[1] - self.r[0]) / 2, (self.r[1] - self.r[0]) / 4)
                value = np.clip(value, self.r[0], self.r[1])
                randval.append(value)
        elif self.distribution_type == "binomial":
            # Binomial distribution
                for _ in range(self.n):
                    value = np.random.binomial(1, 0.5) * (self.r[1] - self.r[0]) + self.r[0]
                    randval.append(value)
        elif self.distribution_type == "poisson":
            # Poisson distribution
            for _ in range(self.n):
                value = np.random.poisson((self.r[1] - self.r[0]) / 2) + self.r[0]
                randval.append(value)
        elif self.distribution_type == "bayesian":
            # Bayesian distribution (Beta distribution as an example)
            alpha = 2
            beta = 2
            for _ in range(self.n):
                value = np.random.beta(alpha, beta) * (self.r[1] - self.r[0]) + self.r[0]
                randval.append(value)
        else:
            print("Invalid distribution type:", self.distribution_type)
            print("Please nominate a value uniform, normal, binominal, poisson or bayesian")

        return randval




#quit();


'''
	process_values()
	


  # Process line based on column 1 value
  if column_1 == 'Option1':
  # Code to process for Option1
  pass
  elif column_1 == 'Option2':
  # Code to process for Option2
  pass
  elif column_1 == 'Option3':
  # Code to process for Option3
  pass
  else:
  # Code to process for other options or handle unrecognized values
  pass


def process_values(value_list):
  for value in value_list:
  if ',' in value:
  # Value is a set of comma-delimited categorical values
  categorical_values = value.split(',')
  print("Categorical values:", categorical_values)
  elif '-' in value:
  # Value is a numerical range
  start, end = value.split('-')
  start = int(start)
  end = int(end)
  print("Numerical range:", start, "-", end)
  else:
  print("Unrecognized format:", value)


'''




