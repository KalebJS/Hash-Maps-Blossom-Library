# creating a hash map for indexing names and meanings of various flowers
# uses separate chaining for incidents of collision

from linked_list import Node, LinkedList
from blossoms_lib import flower_definitions

class HashMap :
    def __init__(self, size) :
        self.array_size = size
        self.array = [LinkedList for i in range(size)]

    def hash (self, key) :
        return sum(key.encode())

    def compress (self, hash_code) :
        return hash_code % self.array_size

    def assign (self, key, value) :
        hash_code = hash(key)
        array_position = self.compress(hash_code)
        payload = Node([key, value])
        list_at_array = self.array[array_position]
        for item in list_at_array : #this should work, but the __iter__ in the othe linked_list.py file is not working
            if item[0] == key :
                item = [key, value]
                return
        list_at_array.insert(payload)
        return

    def retrieve (self, key) :
        hash_code = hash(key)
        array_position = compress(hash_code)
        list_at_array = self.array[array_position]
        for item in list_at_array :
            if item[0] == key :
                return item[1]
        return None
    
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions :
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))