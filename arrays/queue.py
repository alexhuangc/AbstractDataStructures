from .abc_array import Array

class Queue(Array):
    def __init__(self) -> None:
        super().__init__()
        self.__head_index = 0
        self.__tail_index = 0
        self.__is_empty = True
        self.__array_size = 0
    
    def append(self, __value, /):
        # fast implementation and wrapping
        pass
        

    def pop(self) -> object:
        # fast implementation and wrapping
        pass

    def peek(self) -> object:
        return self.__array[self.__head_index]

    def count(self, __value) -> int:
        count = 0
        for i in range(len(self)):
            if self.__array[i] == __value:
                count += 1
        return count

    def is_empty(self) -> bool:
        return self.__is_empty

    def copy(self) -> 'Queue':
        copy_queue = Queue()
        copy_queue.__array = self.__array.copy()
        copy_queue.__length = self.__length
        copy_queue.__head_index = self.__head_index
        copy_queue.__tail_index = self.__tail_index
        return copy_queue

    def __at_capacity(self) -> bool:
        # return len(self) =
        pass
        


if __name__ == '__main__':
    q = Queue()
    