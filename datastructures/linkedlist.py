from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list: LinkedList[T] = LinkedList(data_type=data_type)

        for item in sequence:
            linked_list.append(item)

        return linked_list

    def append(self, item: T) -> None:
        
        # 1. Check that item is an instance of data_type
        # 2. Instantiate a new node with the data

        new_node: LinkedList.Node = LinkedList.Node(data = item)

        #3 Append the item at the end
        #3A Empty
        if self.empty:
            self.head = self.tail = new_node

        #3B Not empty
        else:
            if self.tail:
                self.tail.next = new_node
            
            new_node.previous = self.tail

            self.tail = new_node



        self.count += 1



    def prepend(self, item: T) -> None:
        raise NotImplementedError("LinkedList.prepend is not implemented")

    def insert_before(self, target: T, item: T) -> None:
        # raise an TypeError if target or item are not the correct types
        # raise a ValueError if target is not even in the darn list

        if self.head and self.head.data == target:
            self.prepend(item)
            return


        travel = self.head

        while travel is not None:

            if travel.data == target:
                break

            travel = travel.next
        
        if travel is None:
            raise ValueError(f"The target item {target} is not in the linked list.")
        
        self.count += 1


    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        raise NotImplementedError("LinkedList.front is not implemented")

    @property
    def back(self) -> T:
        if not self.tail or self.count == 0:
            raise ValueError('The Linked List is empty')
        
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None and self.tail is None and self.count == 0

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self



    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> Iterator[T]:
        travel = self.tail

        while travel is not None:
            yield travel.data

            travel = travel.previous

        

    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
