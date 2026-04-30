import sys
from cell_split_lib import calculate_split

if len(sys.argv) != 3:
    print("Usage: python cell_split_cli.py <total_volume> <split_ratio>")
    sys.exit()

total_volume = float(sys.argv[1])
split_ratio = float(sys.argv[2])

cells, medium = calculate_split(total_volume, split_ratio)

print("\n--- Cell Splitting Instructions ---")
print(f"Take {cells:.2f} mL of cells")
print(f"Add {medium:.2f} mL of fresh medium")
print(f"Final volume: {total_volume:.2f} mL")
