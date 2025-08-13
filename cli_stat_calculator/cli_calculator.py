# This file is the main entry point of the program. It acts as the user interface (via command line), guiding the user through selecting what they want to analyze, reading the file, and printing results or saving reports.

from file_handler import CSVReader
from stats_module import StatisticsCalculator
from correlation_module import CorrelationAnalyzer
from hypothesis_module import HypothesisTester

def print_menu():
    print("\nCLI Statistical Calculator")
    print("==========================")
    print("1. Descriptive Statistics (Mean, Median, etc.)")
    print("2. Correlation Analysis")
    print("3. Hypothesis Testing")
    print("4. Exit")

def handle_descriptive_stats(data):
    stats = StatisticsCalculator(data)
    print("\nDescriptive Statistics:")
    print(f"Mean: {stats.mean():.2f}")
    print(f"Median: {stats.median()}")
    print(f"Mode: {stats.mode()}")
    print(f"Standard Deviation: {stats.standard_deviation():.2f}")
    print(f"Variance: {stats.variance():.2f}")
    print(f"Skewness: {stats.skewness():.2f}")
    print(f"Kurtosis: {stats.kurtosis():.2f}")
    print("\nFrequency Distribution:")
    for k, v in stats.frequency_distribution().items():
        print(f"  {k}: {v}")
    print("\nHistogram:\n")
    print(stats.text_histogram())

    save = input("Save this report to file? (y/n): ").strip().lower()
    if save == 'y':
        stats.generate_report("results/analysis_report.txt")
        print("Report saved to results/analysis_report.txt")

def handle_correlation():
    file_path = input("Enter CSV path: ")
    column1 = input("Enter first column name: ")
    column2 = input("Enter second column name: ")

    try:
        data = CSVReader.load_csv_as_dict(file_path)
        corr = CorrelationAnalyzer(data, column1, column2)
        value = corr.pearson_correlation()
        print(f"\nPearson Correlation Coefficient between '{column1}' and '{column2}': {value:.4f}")
    except Exception as e:
        print(f"Error: {e}")

def handle_hypothesis_testing():
    file_path = input("Enter CSV path: ")
    column = input("Enter column name to test: ")

    try:
        data = CSVReader.load_csv_as_dict(file_path)
        tester = HypothesisTester(data)
        print("\n1. One-sample t-test")
        print("2. Independent two-sample t-test")
        print("3. Chi-square test (categorical data)")

        choice = input("Choose a test: ")

        if choice == "1":
            t_stat, p_val = tester.one_sample_t_test(column, popmean=0)
            print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")
        elif choice == "2":
            col2 = input("Enter second column name: ")
            t_stat, p_val = tester.two_sample_t_test(column, col2)
            print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")
        elif choice == "3":
            observed = tester.extract_observed_frequencies(column)
            chi2, p_val = tester.chi_square_test(observed)
            print(f"Chi-square: {chi2:.4f}, p-value: {p_val:.4f}")
        else:
            print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter CSV path: ")
            try:
                data = CSVReader.load_csv(file_path)
                handle_descriptive_stats(data)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            handle_correlation()

        elif choice == "3":
            handle_hypothesis_testing()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()


# What This File Covers
# Section	Purpose
# print_menu()	Displays user options
# handle_descriptive_stats()	Calls StatisticsCalculator for numeric analysis
# handle_correlation()	Calls CorrelationAnalyzer to calculate correlation
# handle_hypothesis_testing()	Uses HypothesisTester for t-tests or chi-square
# main()	Manages user interaction loop

# Input Validation
# Checks that the CSV file is provided

# Handles errors like missing columns, non-numeric data, or malformed files

# Confirms with user before saving reports