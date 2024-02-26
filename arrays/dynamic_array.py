from .array import Array

class List(Array):
    def __init__(self) -> None:
        self.array = []
        self.length = 0

    def append(self, obj, /) -> None:
        self.length += 1
        self.array.append(obj)
    
    def pop(self, index: int=-1, /) -> object:
        self.length -= 1
        return self.array.pop(index)

    def insert(self, index, object, /) -> None:
        self.length += 1
        self.array.insert(index, object)
    
    def count(self, obj, /) -> int:
        count = 0
        for i in range(self.length):
            if self.array[i] == obj:
                count += 1
        return count
    
    def remove(self, obj, /) -> None:
        for i in range(self.length):
            if self.array[i] == obj:
                self.length -= 1
                self.array.pop(i)
                return
        return

    def extend(self, list: 'List') -> None:
        self.length += list.length
        self.array = self.array + list.array

    def copy(self) -> 'List':
        array_copy = List()
        for i in range(self.length):
            array_copy.append(self.array[i])
        return array_copy
    
    # def __len__(self) -> int:
    #     return self.length
    
    # def __eq__(self, __value: 'List') -> bool:
    #     if len(self) != len(__value):
    #         return False
        
    #     for i in range(len(self)):
    #         if self.array[i] != __value.array[i]:
    #             return False
        
    #     return True
    
    # def __ge__(self, other: 'List') -> bool:
    #     for i in range(max(len(self), len(other))):
    #         # (self is shorter) => (self < other)
    #         if i == len(self):
    #             return False
            
    #         # (other is shorter) => (self > other)
    #         if i == len(other):
    #             return True
            
    #         # (self[i] > other[i]) => (self > other)
    #         if self[i] > other[i]:
    #             return True
    #         # (self[i] < other[i]) => (self < other)
    #         elif self[i] < other[i]:
    #             return False
    #         # (self[i] == other[i]) => (unsure)
            
    #     # Both List are equal
    #     return True
    
    # def __gt__(self, other: 'List') -> bool:
    #     for i in range(max(len(self), len(other))):
    #         # (self is shorter) => (self < other)
    #         if i == len(self):
    #             return False
            
    #         # (other is shorter) => (self > other)
    #         if i == len(other):
    #             return True
            
    #         # (self[i] > other[i]) => (self > other)
    #         if self[i] > other[i]:
    #             return True
    #         # (self[i] < other[i]) => (self < other)
    #         elif self[i] < other[i]:
    #             return False
    #         # (self[i] == other[i]) => (unsure)
            
    #     # Both List are equal
    #     return False

    # def __le__(self, other: 'List') -> bool:
    #     for i in range(max(len(self), len(other))):
    #         # (self is shorter) => (self < other)
    #         if i == len(self):
    #             return True
            
    #         # (other is shorter) => (self > other)
    #         if i == len(other):
    #             return False
            
    #         # (self[i] > other[i]) => (self > other)
    #         if self[i] > other[i]:
    #             return False
    #         # (self[i] < other[i]) => (self < other)
    #         elif self[i] < other[i]:
    #             return True
    #         # (self[i] == other[i]) => (unsure)
            
    #     # Both List are equal
    #     return True

    # def __lt__(self, other: 'List') -> bool:
    #     for i in range(max(len(self), len(other))):
    #         # (self is shorter) => (self < other)
    #         if i == len(self):
    #             return True
            
    #         # (other is shorter) => (self > other)
    #         if i == len(other):
    #             return False
            
    #         # (self[i] > other[i]) => (self > other)
    #         if self[i] > other[i]:
    #             return False
    #         # (self[i] < other[i]) => (self < other)
    #         elif self[i] < other[i]:
    #             return True
    #         # (self[i] == other[i]) => (unsure)
            
    #     # Both List are equal
    #     return False
    
    # def __contains__(self, obj, /) -> bool:
    #     if self.length == 0: return False

    #     for item in self.array:
    #         if item == obj:
    #             return True
        
    #     return False

    # def __add__(self, other: 'List') -> 'List':
    #     added_list = self.copy()
    #     for i in range(len(other)):
    #         added_list.append(other[i])
    #     return added_list

    # def __iadd__(self, other: 'List') -> None:
    #     self.array += other.array
    #     self.length += other.length
    #     return self
    
    # def __getitem__(self, key) -> object:
    #     return self.array[key]

    # def __setitem__(self, key, value) -> None:
    #     self.array[key] = value
    #     return

    # def __str__(self) -> str:
    #     output = "["
    #     for i in range(len(self)):
    #         output += str(self.array[i])
    #         if i != len(self)-1:
    #             output += ", "
    #     output += "]"
    #     return output
    
    # def __repr__(self) -> str:
    #     return str(self)
    

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