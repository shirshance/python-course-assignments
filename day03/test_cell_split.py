from cell_split_lib import split_cells

def test_split_1_to_10():
    cells, medium = split_cells(10, 10)
    assert cells == 1
    assert medium == 9

def test_split_1_to_5():
    cells, medium = split_cells(10, 5)
    assert cells == 2
    assert medium == 8

def test_split_1_to_3():
    cells, medium = split_cells(12, 3)
    assert cells == 4
    assert medium == 8
