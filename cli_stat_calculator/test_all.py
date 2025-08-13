#  test_all.py module. This file contains unit tests for your core logic: statistical calculations, correlation, and hypothesis testing. These tests will help ensure your calculator is functioning correctly and handles edge cases.

import unittest
from stats_module import StatisticsCalculator
from correlation_module import CorrelationAnalyzer
from hypothesis_module import HypothesisTester

class TestStatisticsCalculator(unittest.TestCase):
    def setUp(self):
        self.data = [10, 20, 20, 30, 40]
        self.stats = StatisticsCalculator(self.data)

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 24)

    def test_median(self):
        self.assertEqual(self.stats.median(), 20)

    def test_mode(self):
        self.assertEqual(self.stats.mode(), 20)

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.stats.standard_deviation(), 11.40, places=2)

    def test_variance(self):
        self.assertAlmostEqual(self.stats.variance(), 130, places=0)

    def test_skewness(self):
        skew = self.stats.skewness()
        self.assertIsInstance(skew, float)

    def test_kurtosis(self):
        kurt = self.stats.kurtosis()
        self.assertIsInstance(kurt, float)

class TestCorrelationAnalyzer(unittest.TestCase):
    def test_pearson_correlation(self):
        data = {
            "X": [1, 2, 3, 4],
            "Y": [10, 20, 30, 40]
        }
        corr = CorrelationAnalyzer(data, "X", "Y")
        result = corr.pearson_correlation()
        self.assertAlmostEqual(result, 1.0, places=4)

class TestHypothesisTester(unittest.TestCase):
    def setUp(self):
        self.data = {
            "SampleA": [5, 7, 9, 6, 8],
            "SampleB": [4, 5, 6, 7, 5],
            "Category": ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']
        }
        self.tester = HypothesisTester(self.data)

    def test_one_sample_t_test(self):
        t_stat, p_val = self.tester.one_sample_t_test("SampleA", popmean=6)
        self.assertIsInstance(t_stat, float)
        self.assertIsInstance(p_val, float)

    def test_two_sample_t_test(self):
        t_stat, p_val = self.tester.two_sample_t_test("SampleA", "SampleB")
        self.assertIsInstance(t_stat, float)
        self.assertIsInstance(p_val, float)

    def test_chi_square(self):
        observed = self.tester.extract_observed_frequencies("Category")
        chi2, p_val = self.tester.chi_square_test(observed)
        self.assertIsInstance(chi2, float)
        self.assertIsInstance(p_val, float)

if __name__ == '__main__':
    unittest.main()


# Key Testing Areas
# Module	What’s Tested
# StatisticsCalculator	All core stats including mean, std dev, skewness, kurtosis
# CorrelationAnalyzer	Pearson correlation between two columns
# HypothesisTester	One-sample t-test, two-sample t-test, chi-square test

# How to Run the Tests
# Run this file using the terminal:
# python -m unittest test_suite/test_all.py
# Or simply:
# python test_all.py

# Why Unit Tests Matter
# Catches bugs early

# Confirms correct math

# Prevents regressions

# Boosts confidence in results