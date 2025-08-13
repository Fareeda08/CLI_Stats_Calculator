## This module, which performs:
#  One-sample t-test
# Independent two-sample t-test
# Chi-square test (for categorical/frequency data)
# These are foundational for drawing inferences from data, especially in real-world decision-making scenarios.

from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
import numpy as np

class HypothesisTester:
    def __init__(self, data: dict):
        """
        Initialize with a dictionary of columns from CSV file.
        Each key is a column name; each value is a list of entries.
        """
        self.data = data

    def _clean_column(self, column_name):
        """
        Converts column values to float and removes non-numerics.
        """
        column = self.data.get(column_name, [])
        cleaned = []
        for val in column:
            try:
                cleaned.append(float(val))
            except (ValueError, TypeError):
                continue
        return cleaned

    def one_sample_t_test(self, column_name, popmean=0):
        """
        Performs one-sample t-test.
        Compares sample mean to population mean (default = 0).
        """
        sample = self._clean_column(column_name)
        if len(sample) < 2:
            raise ValueError("Not enough data for one-sample t-test.")
        t_stat, p_val = ttest_1samp(sample, popmean)
        return t_stat, p_val

    def two_sample_t_test(self, col1, col2):
        """
        Performs independent two-sample t-test.
        Compares the means of two independent groups.
        """
        sample1 = self._clean_column(col1)
        sample2 = self._clean_column(col2)

        if len(sample1) < 2 or len(sample2) < 2:
            raise ValueError("Both samples must have at least 2 numeric entries.")
        t_stat, p_val = ttest_ind(sample1, sample2, equal_var=False)
        return t_stat, p_val

    def extract_observed_frequencies(self, column_name):
        """
        Returns a dictionary of category: count from a column.
        Used for chi-square test.
        """
        column = self.data.get(column_name, [])
        freq = {}
        for val in column:
            val = str(val).strip()
            if val:
                freq[val] = freq.get(val, 0) + 1
        return freq

    def chi_square_test(self, observed_freq_dict):
        """
        Performs chi-square goodness-of-fit test.
        Takes a dictionary of observed frequencies.
        """
        observed = np.array(list(observed_freq_dict.values()))
        if len(observed) < 2:
            raise ValueError("Need at least two categories for chi-square test.")
        chi2, p_val, _, _ = chi2_contingency([observed])
        return chi2, p_val


# What’s in This Module?
# Method	Purpose
# one_sample_t_test()	Test if sample mean is significantly different from population mean
# two_sample_t_test()	Compare two groups’ means
# extract_observed_frequencies()	Get counts for categories (for chi-square test)
# chi_square_test()	Test whether observed frequencies differ from expected

#  Sample Outputs
#  One-Sample T-Test:
#  Two-Sample T-Test:
#  Chi-Square Test:

#  Concepts Demonstrated:
# Hypothesis testing using scipy.stats
# Data cleaning and type safety
# Error handling for insufficient data
# Simple abstraction of statistical testing workflows