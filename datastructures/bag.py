from typing import Dict, Iterable
from datastructures.ibag import IBag, T


# comment

class Bag(IBag[T]):
    def __init__(self, *items: T) -> None: # modify typehint
        self.__bag: Dict[T, int] = {}

        if items is not None:
            for item in items:
                self.add(item)
                

    def add(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1

    def remove(self, item: T) -> None:
        raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        return self.__bag.keys()

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")