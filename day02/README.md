# Cell Splitting Calculator

## Description

This program helps calculate how to split cells in cell culture.

In the lab, when passaging cells, we usually take a fraction of the culture (for example 1:10) and add fresh medium to reach the same final volume. This script calculates how much volume of cells to take and how much fresh medium to add.

The program uses command-line arguments and includes validation to make sure the values entered are positive numbers.

---

## How to use

Run the program from the terminal:

```bash
python cell_split_cli.py <total_volume> <split_ratio>
```

Example:

```bash
python cell_split_cli.py 10 10
```

Where:

* `10` = total culture volume in mL
* `10` = split ratio for a 1:10 split

---

## What the program does

The program calculates:

* Volume of cells to take
* Volume of fresh medium to add
* Final volume

It also checks for invalid values such as:

* split ratio equal to 0
* negative numbers

---

## Example

### Input

```bash
python cell_split_cli.py 10 10
```

### Output

```text
--- Cell Splitting Instructions ---
Take 1.00 mL of cells
Add 9.00 mL of fresh medium
Final volume: 10.00 mL
```

---

## AI usage

I used ChatGPT.

Prompt used:

"can you help me write a python code for splitting cells in lab? i want to enter total volume and split ratio (like 1:10) and get how much cells to take and how much media to add"
