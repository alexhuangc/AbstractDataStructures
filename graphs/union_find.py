class UnionFind():
    def __init__(self) -> None:
        self.__object_to_index_mapping: dict[object, int] = {}
        self.__index_to_object_mapping: list[object] = []
        self.__connections: list[int] = []
        self.__length: int = 0

    def add_node(self, node: object) -> None:
        self.__object_to_index_mapping[node] = self.__length
        self.__index_to_object_mapping.append(node)
        self.__connections.append(self.__length)
        self.__length += 1

    def union(self, node1: object, node2: object) -> None:
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        root_node2_index = self.__object_to_index_mapping[root_node2]
        self.__connections[root_node2_index] = self.__object_to_index_mapping[root_node1]
        # TODO: Optimization by union shorter tree to longer tree

    def find(self, node: object) -> object:
        node_index = self.__object_to_index_mapping[node]
        current_index = node_index
        while current_index != self.__connections[current_index]:
            current_index = self.__connections[current_index]
        return self.__index_to_object_mapping[current_index]
        # TODO: Optimization by compression of tree

    def __str__(self) -> str:
        output = f"Union Find\n-----------\n{'Object Mapping:':<20} {self.__index_to_object_mapping}\n{'Index Mapping:':<20} {self.__connections}\n{'Length:':<20} {self.__length}"
        return output


if __name__ == "__main__":
    uf = UnionFind()
    for i in range(10):
        uf.add_node(i)
    uf.union(1, 3)
    uf.union(1, 4)
    uf.union(1, 5)
    uf.union(1, 8)
    print(uf)

    print(uf.find(9))
    print(type(uf.find(3)))
            
 