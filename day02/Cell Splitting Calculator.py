# cell_split_cli.py

import argparse

def split_cells(total_volume, split_ratio):
    if total_volume <= 0:
        raise ValueError("Total volume must be greater than 0.")

    if split_ratio <= 0:
        raise ValueError("Split ratio must be greater than 0.")

    cells_to_take = total_volume / split_ratio
    medium_to_add = total_volume - cells_to_take

    return cells_to_take, medium_to_add


# Create argument parser
parser = argparse.ArgumentParser(
    description="Cell Splitting Calculator"
)

# Add command-line arguments
parser.add_argument(
    "total_volume",
    type=float,
    help="Total volume of cells in mL"
)

parser.add_argument(
    "split_ratio",
    type=float,
    help="Split ratio (e.g., 10 for 1:10)"
)

# Parse arguments
args = parser.parse_args()

try:
    cells_to_take, medium_to_add = split_cells(
        args.total_volume,
        args.split_ratio
    )

    print("\n--- Cell Splitting Instructions ---")
    print(f"Take {cells_to_take:.2f} mL of cells")
    print(f"Add {medium_to_add:.2f} mL of fresh medium")
    print(f"Final volume: {args.total_volume:.2f} mL")

except ValueError as error:
    print("Error:", error)
