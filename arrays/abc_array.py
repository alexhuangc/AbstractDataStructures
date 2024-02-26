from abc import ABC, abstractmethod

class Array(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__array = []
        self.__length = 0

    @abstractmethod
    def append(self, __value) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def count(self, __value) -> int:
        pass

    @abstractmethod
    def copy(self) -> 'Array':
        pass

    def __iter__(self):
        return iter(self.__array)

    def __len__(self) -> int:
        return self.__length
    
    def __eq__(self, __value: 'Array') -> bool:
        if len(self) != len(__value):
            return False
        
        for i in range(len(self)):
            if self.__array[i] != __value.__array[i]:
                return False
        
        return True
    
    def __ge__(self, other: 'Array') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return False
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return True
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return True
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return False
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return True
    
    def __gt__(self, other: 'Array') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return False
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return True
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return True
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return False
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return False

    def __le__(self, other: 'Array') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return True
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return False
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return False
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return True
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return True

    def __lt__(self, other: 'Array') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return True
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return False
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return False
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return True
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return False
    
    def __contains__(self, obj, /) -> bool:
        if len(self) == 0: return False

        for item in self.__array:
            if item == obj:
                return True
        
        return False

    def __add__(self, other: 'Array') -> 'Array':
        added_list = self.copy()
        for i in range(len(other)):
            added_list.append(other[i])
        return added_list

    def __iadd__(self, other: 'Array') -> None:
        self.__array += other.__array
        self.__length += len(other)
        return self
    
    def __getitem__(self, key) -> object:
        return self.__array[key]

    def __setitem__(self, key, value) -> None:
        self.__array[key] = value
        return

    def __str__(self) -> str:
        output = "["
        for i in range(len(self)):
            output += str(self.__array[i])
            if i != len(self)-1:
                output += ", "
        output += "]"
        return output
    
    def __repr__(self) -> str:
        return str(self)
    