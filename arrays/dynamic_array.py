from .abc_array import Array

class List(Array):
    def __init__(self) -> None:
        super().__init__()

    def append(self, obj, /) -> None:
        self.__length += 1
        self.__array.append(obj)
    
    def pop(self, index: int=-1, /) -> object:
        self.__length -= 1
        return self.__array.pop(index)

    def insert(self, index, object, /) -> None:
        self.__length += 1
        self.__array.insert(index, object)
    
    def count(self, obj, /) -> int:
        count = 0
        for i in range(self.__length):
            if self.__array[i] == obj:
                count += 1
        return count
    
    def remove(self, obj, /) -> None:
        for i in range(self.__length):
            if self.__array[i] == obj:
                self.__length -= 1
                self.__array.pop(i)
                return
        return

    def extend(self, list: 'List') -> None:
        self.__length += list.__length
        self.__array = self.__array + list.__array

    def copy(self) -> 'List':
        copy_list = List()
        copy_list.__array = self.__array.copy()
        copy_list.__length = self.__length
        return copy_list

if __name__ == '__main__':
    mylist = List()
    slist = List()
    for i in range(10):
        mylist.append(i)
        slist.append(i+1)
    # print(mylist + slist)
    mylist += slist 
    print(mylist)

    # list()