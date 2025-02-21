

from datastructures.array2d import Array2D
from datastructures.bag import Bag
from tests.car import Car


def main():
    
    data_type = Car

    rows_len, cols_len = 3, 2

    sequence = [[data_type() for _ in range(cols_len)] for _ in range(rows_len)]

    sequence2 = []
    for row_index in range(rows_len):
        sequence.append([])

    for row_index in range(rows_len):
        for col_index in range(cols_len):
            sequence2[row_index].append(data_type())

    return Array2D(starting_sequence=sequence, data_type=data_type)

    



if __name__ == '__main__':
    main()
