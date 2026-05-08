# Cell Splitting Calculator – Extended Version

## Description

This program helps calculate how to split cells in cell culture experiments.

In the lab, when passaging cells, we usually take a fraction of the culture (for example 1:10) and add fresh medium to reach the same final volume. This script calculates how much volume of cells to take and how much fresh medium to add.

The extended version also allows the user to enter the number of wells, plates, or flasks they want to prepare. The program then calculates the total amount of cells and medium needed for the entire experiment.

---

## How to use

Run the Python file:

```bash id="fsgm2g"
python cell_split_input.py
```

The program will ask for:

* Final volume per well/plate/flask (mL)
* Split ratio
* Number of wells/plates/flasks

---

## What the program does

For each sample, the program calculates:

* Volume of cells to take
* Volume of fresh medium to add

It also calculates the total volumes needed for all samples together.

---

## Example

### Input

```text id="8w7t7u"
Enter final volume per well/plate (mL): 10
Enter split ratio (e.g., 10 for 1:10): 10
Enter number of wells/plates/flasks: 3
```

### Output

```text id="5daxea"
--- Cell Splitting Instructions ---
For each well/plate/flask:
Take 1.00 mL of cells
Add 9.00 mL of fresh medium

--- Total Volume Needed ---
Total cells needed: 3.00 mL
Total fresh medium needed: 27.00 mL
Total final volume: 30.00 mL
```

---

## AI usage

I used ChatGPT.

Prompt used:

"can you help me write a python code for splitting cells in lab? i want to enter total volume and split ratio (like 1:10) and get how much cells to take and how much media to add"

I also used ChatGPT to help extend the program by adding support for multiple wells/plates/flasks and calculating total required volumes.

