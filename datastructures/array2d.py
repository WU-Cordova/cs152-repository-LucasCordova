from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):
    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def __getitem__(self, column_index: int) -> T:
            if column_index < 0 or column_index >= self.num_columns: raise IndexError(f'Column index {column_index} out of bounds.')
            return self.array[self.index_mapper(column_index)]
        
        def index_mapper(self, column_index: int) -> int:
            return self.row_index * self.num_columns + column_index
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.array[self.index_mapper(column_index)] = value
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns - 1, -1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence) or isinstance(starting_sequence, str): 
            raise ValueError(f'Input `{starting_sequence}` must be a sequence of sequences.')
        if not all(isinstance(row, Sequence) for row in starting_sequence): 
            raise ValueError(f'Input `{starting_sequence}` must be a sequence containing sequences.')

        self.__num_rows = len(starting_sequence)
        self.__num_columns = len(starting_sequence[0])
        if self.__num_rows > 0 and not all(len(row) == self.__num_columns for row in starting_sequence): 
            raise ValueError(f'Input `{starting_sequence}` must be a sequence of sequences with the same length.')
        
        self._data_type = data_type
        if not all(isinstance(item, self._data_type) for row in starting_sequence for item in row): 
            raise ValueError('All items must be of the same type.')
        
        self.__array = Array([item for row in starting_sequence for item in row], data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D[T]:
        return Array2D([[data_type() for _ in range(cols)] for _ in range(rows)], data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index < 0 or row_index >= self.__num_rows: raise IndexError(f'Row index {row_index} out of bounds.')
        return Array2D.Row(row_index, self.__array, self.__num_columns)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.__num_rows):
            yield self[row_index]
    
    def __reversed__(self):
        for row_index in range(self.__num_rows - 1, -1, -1):
            yield self[row_index]
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array2D): return False
        if self.__num_rows != other.__num_rows or self.__num_columns != other.__num_columns: return False
        return self.__array == other.__array
    
    def __len__(self): return self.__num_rows
    def __str__(self) -> str: return f'[{", ".join(f"{str(row)}" for row in self)}]'
    def __repr__(self) -> str: return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

# Note to Future Self
# add the __eq__ method to both Array2D and Row