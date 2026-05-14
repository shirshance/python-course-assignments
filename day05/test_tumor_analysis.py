import pandas as pd
from mice_tumor_growth import excel_column_to_index, read_tumor_data


def test_excel_column_to_index():
    assert excel_column_to_index("A") == 0
    assert excel_column_to_index("E") == 4
    assert excel_column_to_index("AB") == 27
    assert excel_column_to_index("AI") == 34


def test_read_tumor_data(tmp_path):
    fake_excel = tmp_path / "fake_mice_tumor_size.xlsx"

    data = pd.DataFrame([[0 for _ in range(35)] for _ in range(32)])

    data.iloc[10, 4] = 100   # E11, WT1 day 7
    data.iloc[15, 4] = 200   # E16, WT2 day 7
    data.iloc[20, 4] = 300   # E21, KO24 day 7
    data.iloc[25, 4] = 400   # E26, KO27 day 7
    data.iloc[30, 4] = 500   # E31, KO28 day 7

    data.to_excel(fake_excel, index=False, header=False)

    days, tumor_data = read_tumor_data(fake_excel)

    assert days == [7, 11, 14, 18, 21, 25, 33, 37, 44, 52]

    assert tumor_data["WT1"][0] == 100
    assert tumor_data["WT2"][0] == 200
    assert tumor_data["KO24"][0] == 300
    assert tumor_data["KO27"][0] == 400
    assert tumor_data["KO28"][0] == 500
