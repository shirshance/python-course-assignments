def split_cells(total_volume, split_ratio):
    if total_volume <= 0:
        raise ValueError("Total volume must be positive")

    if split_ratio <= 1:
        raise ValueError("Split ratio must be greater than 1")

    cells_to_take = total_volume / split_ratio
    medium_to_add = total_volume - cells_to_take

    return cells_to_take, medium_to_add
