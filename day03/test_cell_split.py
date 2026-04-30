from cell_split_lib import calculate_split

def test_split_1_to_10():
    cells, medium = calculate_split(10, 10)
    assert cells == 1
    assert medium == 9

def test_split_1_to_5():
    cells, medium = calculate_split(10, 5)
    assert cells == 2
    assert medium == 8

def test_split_1_to_3():
    cells, medium = calculate_split(12, 3)
    assert cells == 4
    assert medium == 8
