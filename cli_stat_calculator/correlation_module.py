# This module computes Pearson’s correlation coefficient between two numerical columns in a CSV file, which helps determine the strength and direction of a linear relationship.

from scipy.stats import pearsonr

class CorrelationAnalyzer:
    def __init__(self, data: dict, col1: str, col2: str):
        """
        Initializes the analyzer with a dictionary of data and the two columns to compare.
        """
        if col1 not in data or col2 not in data:
            raise ValueError(f"Columns '{col1}' or '{col2}' not found in data.")

        self.x = self._clean_column(data[col1])
        self.y = self._clean_column(data[col2])

        if len(self.x) != len(self.y):
            raise ValueError("The two columns must have the same number of valid numerical entries.")
        if len(self.x) < 2:
            raise ValueError("Not enough data for correlation analysis.")

    def _clean_column(self, column):
        """
        Converts column values to float, ignoring non-numeric entries.
        """
        cleaned = []
        for val in column:
            try:
                cleaned.append(float(val))
            except ValueError:
                continue
        return cleaned

    def pearson_correlation(self):
        """
        Computes and returns the Pearson correlation coefficient.
        """
        corr, _ = pearsonr(self.x, self.y)
        return corr

# What This File Does
# Function	Purpose
# __init__()	Validates column names and prepares data
# _clean_column()	Converts strings to floats and filters out invalid values
# pearson_correlation()	Uses SciPy to compute Pearson’s r


# Features Demonstrated:
# Dictionary manipulation

# Data cleaning

# Pearson correlation (via scipy.stats)

# Error handling for mismatched or missing data

