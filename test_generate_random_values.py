import unittest
from criteria_mendelian_randomization import Criteria

# Create an instance of the Criteria class
criteria_obj = Criteria([0,10],100,"uniform")

# Call the generate_random_values subroutine
#random_values = criteria_obj.generate_random_values()

# Use the generated random values as needed
#print(random_values)


class TestGenerateRandomValues(unittest.TestCase):

    def test_uniform_distribution(self):
        print("Hello uniform")
        criteria_obj.distribution_type="uniform"
        values = criteria_obj.generate_random_values()
        print (values)
        self.assertEqual(len(values), 100)
        for value in values:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 10)

    def test_normal_distribution(self):
        print("Hello normal")
        criteria_obj.distribution_type="normal"
        values = criteria_obj.generate_random_values()
        print (values)
        self.assertEqual(len(values), 100)

    def test_binomial_distribution(self):
        print("Hello binomial")
        criteria_obj.distribution_type="binomial"
        values = criteria_obj.generate_random_values()
        print (values)
        self.assertEqual(len(values), 100)

    def test_poisson_distribution(self):
        print("Hello poisson")
        criteria_obj.distribution_type="poisson"
        values = criteria_obj.generate_random_values()
        print (values)
        self.assertEqual(len(values), 100)

    def test_bayesian_distribution(self):
        print("Hello bayesian")
        criteria_obj.distribution_type="bayesian"
        values = criteria_obj.generate_random_values()
        print (values)
        self.assertEqual(len(values), 100)
        #print ("PASS Bayesian ", values)


if __name__ == '__main__':
    print("Starting tests")
    unittest.main()

else:
    print("Something failed, please run this as the main program")   
    print (__name__)





