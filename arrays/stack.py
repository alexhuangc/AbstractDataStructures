from .abc_array import Array

class Stack(Array):
    def __init__(self) -> None:
        super().__init__()

    def append(self, __value) -> None:
        self.__array.append(__value)
    
    def pop(self) -> object:
        if len(self) > 0:
            self.__array.pop(-1)
        else:
            raise Exception("Cannot pop from empty stack.")
    
    def count(self, __value) -> int:
        count = 0
        for i in range(len(self)):
            if self.__array[i] == __value:
                count += 1
        return count

    def copy(self) -> 'Stack':
        copy_stack = Stack()
        copy_stack.__array = self.__array.copy()
        copy_stack.__length = self.__length
        return copy_stack