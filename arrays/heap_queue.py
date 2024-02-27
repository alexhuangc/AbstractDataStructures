from .abc_array import Array

class HeapQueue(Array):
    def __init__(self, priority_type: str='min') -> None:
        super().__init__()
        if priority_type == 'min' or priority_type == 'max':
            self.__PRIORITY_TYPE = priority_type
        else:
            raise Exception("priority_type must be either 'min' or 'max' for a min heap or max heap.")

    def append(self, __value) -> None:
        self.__array.append(__value)
        self.__sift_up(self.__array[self.__length])
        self.__length += 1

    def pop(self) -> object:
        
        pass

    def count(self, __value) -> int:
        pass

    def copy(self) -> 'Array':
        pass

    def heapify(self, heapify_list: list) -> None:
        pass

    def __sift_up(self, index):
        current_index = index
        # Min Heap
        if self.__PRIORITY_TYPE == 'min':
            parent_index = (current_index - 1) // 2
            while parent_index >= 0 and self.__array[current_index] < self.__array[parent_index]:
                # Swap child and parent
                child = self.__array[current_index]
                self.__array[current_index] = self.__array[parent_index]
                self.__array[parent_index] = child
                # reset index
                current_index = parent_index
                parent_index = (current_index - 1) // 2
        # Max Heap
        else:
            parent_index = (current_index - 1) // 2
            while parent_index >= 0 and self.__array[current_index] > self.__array[parent_index]:
                # Swap child and parent
                child = self.__array[current_index]
                self.__array[current_index] = self.__array[parent_index]
                self.__array[parent_index] = child
                # reset index
                current_index = parent_index
                parent_index = (current_index - 1) // 2

    