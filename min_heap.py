# Name: Homero Vazquez
# OSU Email: vazqueho@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 3/2/2026
# Description: Min Heap Implementation


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Add a new object to the heap while maintaining heap property.
        """
        #add to the end of the heap
        self._heap.append(node)

        #percolate up
        child_index = self._heap.length() - 1

        while child_index > 0:
            parent_index = (child_index - 1) // 2

            if self._heap[child_index] >= self._heap[parent_index]:
                break

            temp = self._heap[parent_index]
            self._heap[parent_index] = self._heap[child_index]
            self._heap[child_index] = temp

            child_index = parent_index

        # Percolate up
    def is_empty(self) -> bool:
        """
        Return true if the heap is empty; otherwise, it returns False.
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Return the minimum without removing it from the heap.
        If the heap is empty, the method raises exception.
        """
        if self.is_empty():
            raise   MinHeapException

        return self._heap[0]

    def remove_min(self) -> object:
        """
        Remove and return the minimum element.
        Raise MinHeapException if heap is empty.
        """
        if self.is_empty():
            raise MinHeapException

        min_value = self._heap[0]

        # If only one element
        if self._heap.length() == 1:
            self._heap.remove_at_index(0)
            return min_value

        # Move last element to root
        last_index = self._heap.length() - 1
        self._heap[0] = self._heap[last_index]
        self._heap.remove_at_index(last_index)

        # Percolate down
        _percolate_down(self._heap,0)

        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array and builds a proper MinHeap from them.
        """

        self._heap = DynamicArray()
        for i in range(da.length()):
            self._heap.append(da[i])

        # bottom-up
        n = self._heap.length()
        parent = (n // 2) - 1
        while parent >= 0:
            _percolate_down(self._heap, parent)
            parent -= 1

    def size(self) -> int:
        """
        returns the number of items currently stored in heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        clears the content of the heap
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    receives a dynamic array and sorts its content in non-ascending order.
    """
    #build heap from input DA
    heap = MinHeap()
    heap.build_heap(da)

    #Remove objects one by one and place them from end to start
    index = da.length() - 1

    while index >= 0:
        da[index] = heap.remove_min()
        index -= 1


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    percolate downward until heap property is restored.
    """
    size = da.length()

    while True:
        left = 2 * parent + 1
        right = 2 * parent + 2

        # no children
        if left >= size:
            return

        # choose smaller child (tie -> left)
        smallest_child = left
        if right < size and da[right] < da[left]:
            smallest_child = right

        # if parent already <= smallest child, we're done
        if da[parent] <= da[smallest_child]:
            return

        # swap parent with smallest child
        temp = da[parent]
        da[parent] = da[smallest_child]
        da[smallest_child] = temp

        parent = smallest_child


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference the same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
