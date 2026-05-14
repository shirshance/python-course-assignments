import pandas as pd
import matplotlib.pyplot as plt

file_path = "mice_tumor_size.xlsx"

def read_tumor_data(file_path):
    days = [7, 11, 14, 18, 21, 25, 33, 37, 44, 52]

    cells = {
        "WT1":  ["E11", "H11", "K11", "N11", "Q11", "U11", "X11", "AB11", "AE11", "AI11"],
        "WT2":  ["E16", "H16", "K16", "N16", "Q16", "U16", "X16", "AB16", "AE16", "AI16"],
        "KO24": ["E21", "H21", "K21", "N21", "Q21", "U21", "X21", "AB21", "AE21", "AI21"],
        "KO27": ["E26", "H26", "K26", "N26", "Q26", "U26", "X26", "AB26", "AE26", "AI26"],
        "KO28": ["E31", "H31", "K31", "N31", "Q31", "U31", "X31", "AB31", "AE31", "AI31"],
    }

    excel_data = pd.read_excel(file_path, header=None)

    tumor_data = {}

    for mouse, cell_list in cells.items():
        values = []

        for cell in cell_list:
            col_letters = ''.join(filter(str.isalpha, cell))
            row_number = int(''.join(filter(str.isdigit, cell)))

            col_index = excel_column_to_index(col_letters)
            row_index = row_number - 1

            value = excel_data.iloc[row_index, col_index]
            values.append(value)

        tumor_data[mouse] = values

    return days, tumor_data


def excel_column_to_index(column_letters):
    index = 0
    for char in column_letters.upper():
        index = index * 26 + (ord(char) - ord('A') + 1)
    return index - 1


def plot_tumor_growth(days, tumor_data):
    for mouse, values in tumor_data.items():
        plt.plot(days, values, marker="o", label=mouse)

    plt.xlabel("Day")
    plt.ylabel("Tumor volume (mm³)")
    plt.title("Tumor Growth Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("tumor_growth_curve.png", dpi=300)
    plt.show()


def main():
    file_path = "mice_tumor_size.xlsx"

    days, tumor_data = read_tumor_data(file_path)
    plot_tumor_growth(days, tumor_data)


if __name__ == "__main__":
    main()
