class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfuction(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfuction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def get(self, key):
        startslot = self.hashfuction(key)

        data = None
        stop = False
        found = False
        pos = startslot

        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos)
                if pos == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


H = HashTable()
H[54] = 'cat'
H[26] = 'dog'
H[93] = 'lion'
H[17] = 'tiger'
H[77] = 'bird'
H[31] = 'cow'
H[44] = 'goat'
H[55] = 'pig'
H[20] = 'chicken'
H[28] = 'monkey'
H[95] = 'deer'
# H[51] = 'rabbit'


print(H.slots)
print(H.data)
print(H[20])
