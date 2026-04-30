import tkinter as tk
from cell_split_lib import split_cells


def calculate():
    total_volume = float(total_volume_entry.get())
    split_ratio = float(split_ratio_entry.get())

    cells, medium = calculate_split(total_volume, split_ratio)

    result_label.config(
        text=f"Take {cells:.2f} mL of cells\n"
             f"Add {medium:.2f} mL of fresh medium\n"
             f"Final volume: {total_volume:.2f} mL"
    )

window = tk.Tk()
window.title("Cell Splitting Calculator")

tk.Label(window, text="Total volume of cells (mL):").pack()
total_volume_entry = tk.Entry(window)
total_volume_entry.pack()

tk.Label(window, text="Split ratio, e.g. 10 for 1:10:").pack()
split_ratio_entry = tk.Entry(window)
split_ratio_entry.pack()

tk.Button(window, text="Calculate", command=calculate).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
