#This module will take the results from statistical analysis and generate a clean, human-readable .txt report with both the computed values and plain-language interpretations.

from datetime import datetime

class ReportWriter:
    @staticmethod
    def write_descriptive_report(filepath, stats_obj):
        """
        Writes a descriptive statistics report to a .txt file.
        """
        with open(filepath, 'w') as f:
            f.write("STATISTICAL ANALYSIS REPORT\n")
            f.write("===========================\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write(f"Count: {len(stats_obj.data)}\n")
            f.write(f"Mean: {stats_obj.mean():.2f} → Average of dataset\n")
            f.write(f"Median: {stats_obj.median()} → Middle value\n")
            f.write(f"Mode: {stats_obj.mode()} → Most frequent value\n")
            f.write(f"Standard Deviation: {stats_obj.standard_deviation():.2f} → Spread of data\n")
            f.write(f"Variance: {stats_obj.variance():.2f} → Variability measure\n")
            f.write(f"Skewness: {stats_obj.skewness():.2f} → Asymmetry (positive = right-skewed)\n")
            f.write(f"Kurtosis: {stats_obj.kurtosis():.2f} → Tailedness (high = heavy tails)\n")

            f.write("\nFREQUENCY DISTRIBUTION\n")
            f.write("-----------------------\n")
            for value, count in stats_obj.frequency_distribution().items():
                f.write(f"{value}: {count}\n")

            f.write("\nHISTOGRAM (Text-Based)\n")
            f.write("----------------------\n")
            f.write(stats_obj.text_histogram())

            f.write("\nEND OF REPORT\n")

    @staticmethod
    def write_correlation_report(filepath, column1, column2, value):
        with open(filepath, 'w') as f:
            f.write("CORRELATION ANALYSIS REPORT\n")
            f.write("===========================\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Columns Compared: {column1} & {column2}\n")
            f.write(f"Pearson Correlation Coefficient: {value:.4f}\n")

            if abs(value) >= 0.7:
                interpretation = "Strong correlation"
            elif abs(value) >= 0.4:
                interpretation = "Moderate correlation"
            elif abs(value) >= 0.2:
                interpretation = "Weak correlation"
            else:
                interpretation = "Very weak or no correlation"

            f.write(f"Interpretation: {interpretation}\n")
            f.write("\nEND OF REPORT\n")

    @staticmethod
    def write_hypothesis_test_report(filepath, test_type, test_stat, p_value, alpha=0.05):
        with open(filepath, 'w') as f:
            f.write("HYPOTHESIS TESTING REPORT\n")
            f.write("==========================\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Test Type: {test_type}\n")
            f.write(f"Test Statistic: {test_stat:.4f}\n")
            f.write(f"P-Value: {p_value:.4f}\n")

            if p_value < alpha:
                decision = "Reject the null hypothesis (significant result)"
            else:
                decision = "Fail to reject the null hypothesis (not significant)"

            f.write(f"Interpretation: {decision}\n")
            f.write(f"Alpha (Significance Level): {alpha}\n")
            f.write("\nEND OF REPORT\n")


# What Each Method Does
# Method	Description
# write_descriptive_report()	Saves full statistical summary with histogram and meanings
# write_correlation_report()	Logs correlation result and explains strength
# write_hypothesis_test_report()	Stores t-test or chi-square result with interpretation based on p-value


#  Features Demonstrated:
# File writing and formatting

# Clear interpretation for beginner users

# Time-stamped reports

# Plain language explanation of statistical results