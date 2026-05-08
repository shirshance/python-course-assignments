def split_cells(total_volume, split_ratio):
    cells_to_take = total_volume / split_ratio
    medium_to_add = total_volume - cells_to_take
    return cells_to_take, medium_to_add
