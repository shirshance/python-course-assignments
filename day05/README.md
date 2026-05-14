# Tumor Growth Analyzer

This project analyzes tumor growth measurements from mice over time using an Excel file from a laboratory experiment.

The program extracts tumor volume values from an Excel spreadsheet and generates growth curves for five mice:

- WT1
- WT2
- KO24
- KO27
- KO28

Measurements were collected at:

Day 7, 11, 14, 18, 21, 25, 33, 37, 44, and 52.

The output is a tumor growth graph that compares tumor progression across WT and knockout mice.

## Project files

```text
day05/
├── mice_tumor_size.xlsx
├── mice_tumor_growth.py
├── README.md
├── requirements.txt
└── test_tumor_analysis.py
```

## Requirements

Python 3.11+

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

## Run the program

```bash
py mice_tumor_growth.py
```

The script will:

1. Read tumor measurements from the Excel file
2. Extract values from predefined cells
3. Plot tumor growth curves
4. Save:

```text
tumor_growth_curve.png
```

## Libraries used

- pandas
- matplotlib
- openpyxl

## Testing

Run tests using:

```bash
pytest
```

Test 1: checks Excel coordinate conversion
Test 2: checks that tumor values are extracted from the correct cells


