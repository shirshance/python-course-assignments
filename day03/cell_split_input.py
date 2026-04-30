from cell_split_lib import split_cells

total_volume = float(input("Enter total volume of cells (mL): "))
split_ratio = float(input("Enter split ratio (e.g., 10 for 1:10): "))

cells, medium = split_cells(total_volume, split_ratio)

print("\n--- Cell Splitting Instructions ---")
print(f"Take {cells:.2f} mL of cells")
print(f"Add {medium:.2f} mL of fresh medium")
print(f"Final volume: {total_volume:.2f} mL")
