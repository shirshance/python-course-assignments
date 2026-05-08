from cell_split_lib import split_cells

total_volume = float(input("Enter final volume per well/plate (mL): "))
split_ratio = float(input("Enter split ratio (e.g., 10 for 1:10): "))
num_samples = int(input("Enter number of wells/plates/flasks: "))

cells, medium = split_cells(total_volume, split_ratio)

total_cells = cells * num_samples
total_medium = medium * num_samples
total_final_volume = total_volume * num_samples

print("\n--- Cell Splitting Instructions ---")
print(f"For each well/plate/flask:")
print(f"Take {cells:.2f} mL of cells")
print(f"Add {medium:.2f} mL of fresh medium")

print("\n--- Total Volume Needed ---")
print(f"Total cells needed: {total_cells:.2f} mL")
print(f"Total fresh medium needed: {total_medium:.2f} mL")
print(f"Total final volume: {total_final_volume:.2f} mL")
