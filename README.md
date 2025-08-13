#  CLI Statistical Calculator in Python

## Overview
This is a Command-Line Interface (CLI) calculator built in Python that reads numerical data from a CSV file and performs comprehensive statistical analysis, including:

-  Descriptive Statistics (Mean, Median, Mode, Standard Deviation, Variance, Skewness, Kurtosis)
-  Correlation Analysis (Pearson)
-  Hypothesis Testing (T-tests, Chi-square)
-  Frequency Distributions
-  Text-Based Histograms
-  Formatted Report Generation

The project is modular, easy to use, and well-documented for academic or beginner-friendly use.

---

##  Project Structure

cli_stat_calculator/
│
├── cli_calculator.py # Main entry point and CLI
├── stats_module.py # Descriptive statistics functions
├── correlation_module.py # Pearson correlation calculator
├── hypothesis_module.py # T-test and Chi-square tests
├── file_handler.py # CSV reading and input validation
├── report_writer.py # Writes formatted analysis report
├── test_all.py # Unit tests for all modules
│
├── sample_data/
│ └── input_data.csv # Sample CSV input file
│
├── output/
│ ├── analysis_report.txt # Generated statistical output
│ └── images/
│ ├── csv_sample.png
│ ├── histogram_output.png
│ └── output_sample.png
│
├── documentation/
│ ├── User_Manual.pdf # Step-by-step user manual
│ └── Project_Report.pdf # 15-page project write-up
│
└── README.md # You're here!


##  Installation Requirements

Ensure Python 3.10+ is installed. Then install dependencies:

pip install pandas numpy scipy
How to Use
Run the CLI App

python cli_calculator.py
Follow the menu prompts to:

Load your .csv file

Select a column or comparison

View analysis results

Export the report
"# CLI_Stats_Calculator" 
