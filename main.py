from typing_extensions import Self
from typing import Any


class Node:
    value: Any
    next: Self | None
    
    def __init__(self, value: Any, next: Self | None = None):
        self.value = value
        self.next = next
    
    def set_value(self, value: Any):
        self.value = value
        
    def set_next(self, next: Self):
        self.next = next
        

class LinkedList:
    head: Node | None
    
    def __init__(self, head: Node | None = None):
        self.head = head
        
    def add_start(self, value: Any):
        new_node = Node(value, self.head)
        self.head = new_node
        
    def add_end(self, value: Any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        node_iter = self.head
        while node_iter.next is not None:
            node_iter = node_iter.next
        node_iter.next = new_node
        
    def insert_at(self, value: Any, position: int):
        if position == 0:
            return self.add_start(value)
        node_iter = self.head
        position -= 1
        while position:
            if node_iter.next is None:
                raise IndexError("linked list index out of range")
            node_iter = node_iter.next
            position -= 1
        new_node = Node(value, node_iter.next)
        node_iter.next = new_node
        
    def print(self):
        print("[", end="")
        node_iter = self.head
        while node_iter is not None:
            print(f"{node_iter.value} -> ", end="")
            node_iter = node_iter.next
        print("None]")
        
    def pop(self, index: int) -> Any:
        if index == 0:
            if self.head is None:
                raise IndexError("linked list index out of range")
            ref = self.head.next
            val = self.head.value
            self.head = None
            self.head = ref
            return val
        index -= 1
        node_iter = self.head
        while index:
            index -= 1
            if node_iter.next is None:
                raise IndexError("linked list index out of range")
            node_iter = node_iter.next
        ref = node_iter.next.next
        val = node_iter.next.value
        node_iter.next = None
        node_iter.next = ref
        return val
        
    def remove(self, index: int):
        self.pop(index)
        
    def swap(self, idx1: int, idx2: int):
        if idx1 == idx2:
            return
        big = idx1 if idx1 > idx2 else idx2
        small = idx1 if idx1 < idx2 else idx2
        big_node = self.head
        small_node = None
        if small == 0:
            small_node = self.head
        big -= 1
        small -= 1
        while big:
            if big_node.next is None:
                raise IndexError("linked list index out of range")
            if small == 0:
                small_node = big_node
            big_node = big_node.next
            big -= 1
            small -= 1
        small_ref = small_node.next
        big_ref = big_node.next
        small_ref.next, big_ref.next = big_ref.next, small_ref.next
        small_node.next, big_node.next = big_node.next, small_node.next

    def get_ref(self, index: int) -> Node:
        if index == 0:
            return self.head
        index -= 1
        node_iter = self.head
        while index:
            index -= 1
            if node_iter.next is None:
                raise IndexError("linked list index out of range")
            node_iter = node_iter.next
        return node_iter.next
    
    def split_at(self, index: int) -> Self:
        if index == 0:
            ref = self.head
            self.head = None
            return LinkedList(ref)
        index -= 1
        node_iter = self.head
        while index:
            index -= 1
            if node_iter.next is None:
                raise IndexError("linked list index out of range")
            node_iter = node_iter.next
        ref = node_iter.next
        node_iter.next = None
        return LinkedList(ref)
    
    def split_half(self) -> Self:
        length = 0
        node_iter = self.head
        while node_iter is not None:
            node_iter = node_iter.next
            length += 1
        return self.split_at(length//2)
    
    def find(self, value: Any) -> Node:
        node_iter = self.head
        while node_iter is not None:
            if node_iter.value == value:
                return node_iter
            node_iter = node_iter.next
        raise ValueError(f"{value} is not in linked list")

def main():
    List = LinkedList()
    List.add_end(7)
    List.add_end(9)
    List.add_end(1)
    List.add_start(2)
    List.insert_at(3, 2)
    List.print()
    List.remove(3)
    List.print()
    List.add_start(0)
    List.print()
    List.remove(0)
    List.print()
    List.swap(1, 3)
    List.print()
    List2 = List.split_half()
    List.print()
    List2.print()
    
if __name__ == "__main__":
    main()