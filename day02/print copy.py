# Cell Splitting Calculator

# Get input from user
total_volume = float(input("Enter total volume of cells (mL): "))
split_ratio = float(input("Enter split ratio (e.g., 10 for 1:10): "))

# Calculate volumes
cells_to_take = total_volume / split_ratio
medium_to_add = total_volume - cells_to_take

# Output results
print("\n--- Cell Splitting Instructions ---")
print(f"Take {cells_to_take:.2f} mL of cells")
print(f"Add {medium_to_add:.2f} mL of fresh medium")
print(f"Final volume: {total_volume:.2f} mL")
