# This module is where all the key statistical calculations will be performed. 

import statistics
import math
from scipy.stats import skew, kurtosis

class StatisticsCalculator:
    def __init__(self, data: list[float]):
        """
        Initialize the class with a list of numerical data.
        """
        self.data = [float(x) for x in data if isinstance(x, (int, float, str)) and str(x).strip().replace('.', '', 1).isdigit()]
        if not self.data:
            raise ValueError("No valid numerical data provided.")

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        try:
            return statistics.mode(self.data)
        except statistics.StatisticsError:
            return "No unique mode"

    def standard_deviation(self):
        return statistics.stdev(self.data)

    def variance(self):
        return statistics.variance(self.data)

    def skewness(self):
        return skew(self.data)

    def kurtosis(self):
        return kurtosis(self.data)

    def frequency_distribution(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        return dict(sorted(freq.items()))

    def text_histogram(self):
        freq = self.frequency_distribution()
        histogram = ""
        for key, count in freq.items():
            histogram += f"{key:>6}: {'█' * count}\n"
        return histogram

    def generate_report(self, filename: str):
        """
        Generates a text report of all statistics and saves to a file.
        """
        with open(filename, "w") as file:
            file.write("STATISTICAL ANALYSIS REPORT\n")
            file.write("===========================\n\n")
            file.write(f"Count: {len(self.data)}\n")
            file.write(f"Mean: {self.mean():.2f}\n")
            file.write(f"Median: {self.median()}\n")
            file.write(f"Mode: {self.mode()}\n")
            file.write(f"Standard Deviation: {self.standard_deviation():.2f}\n")
            file.write(f"Variance: {self.variance():.2f}\n")
            file.write(f"Skewness: {self.skewness():.2f}\n")
            file.write(f"Kurtosis: {self.kurtosis():.2f}\n\n")
            file.write("Frequency Distribution:\n")
            for k, v in self.frequency_distribution().items():
                file.write(f"  {k}: {v}\n")
            file.write("\nText-Based Histogram:\n")
            file.write(self.text_histogram())


#             Features in This File
# Function	Description
# mean()	Average of the dataset
# median()	Middle value
# mode()	Most frequent value (handles errors)
# standard_deviation()	Measure of spread
# variance()	Square of standard deviation
# skewness()	Measures asymmetry
# kurtosis()	Measures tailedness
# frequency_distribution()	Dictionary of value counts
# text_histogram()	Visualizes frequency distribution using bars
# generate_report()	Saves the analysis to a file