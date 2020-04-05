class hashTable:
    def __init__(self):
        self.size = 511
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return False

    def print(self):
        print('--- Salvador Dalí ---')
        for item in self.map:
            if item is not None:
                print(str(item))
        print()

hashtable = hashTable()

print('Adding...')
hashtable.add('1910', 'Landscape Near Figueras')
hashtable.add('1913', 'Vilabertin')
hashtable.add('1922', 'Cabaret Scene')
hashtable.add('1926', 'The Basket of Bread')
hashtable.add('1930', "L'Age d'Or")
hashtable.add('1931', 'The Persistence of Memory')
hashtable.add('1934', 'The Ghost of Vermeer of Delft Which Can Be Used As a Table')
hashtable.add('1936', 'Lobster Telephone')
hashtable.add('1936', 'Soft Construction with Boiled Beans (Premonition of Civil War)')
hashtable.add('1936', 'Morphological Echo')
hashtable.add('1937', 'Metamorphosis of Narcissus')
hashtable.add('1937', 'Swans Reflecting Elephants')
hashtable.add('1937', 'The Burning Giraffe')
hashtable.add('1937', 'Mae West Lips Sofa')
hashtable.add('1938', 'Apparition of Face and Fruit Dish on a Beach')
hashtable.add('1939', 'Shirley Temple, The Youngest, Most Sacred Monster of the Cinema in Her Time')
print()

hashtable.print()

print('Deleting entry 1922...')
hashtable.delete('1922')
print()

hashtable.print()
print('Painting of the year ' + '1931: ' + hashtable.get('1931'))

