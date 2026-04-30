# Cell Splitting Calculator - Day 03

In this assignment, I continued my Day 02 cell splitting calculator.

The program calculates how much cell suspension to take and how much fresh medium to add according to a desired split ratio.

For example, for a final volume of 10 mL and a split ratio of 1:10:
- take 1 mL of cells
- add 9 mL of fresh medium

## Files

- `cell_split_lib.py` - contains the calculation function.
- `cell_split_input.py` - version that uses standard input with `input()`.
- `cell_split_cli.py` - version that uses command line arguments with `sys.argv`.
- `cell_split_gui.py` - GUI version using `tkinter`.
- `test_cell_split.py` - test file with test cases for the calculation function.

## How to run

Standard input version:

```bash
python cell_split_input.py
