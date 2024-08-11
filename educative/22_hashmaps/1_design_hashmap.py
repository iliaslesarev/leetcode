# A class implementation of the bucket data structure
class Bucket:
    # Initialize bucket here
    def __init__(self):
        self.bucket = []

    # get value from bucket
    def get(self, key):
        for pair_key, pair_value in self.bucket:
            if pair_key == key:
                return pair_value
        return -1

    # put value in bucket
    def update(self, key, value):
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))

    # delete value from bucket
    def remove(self, key):
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                del self.bucket[i]
                return


class DesignHashMap():
    # Use the constructor below to initialize the
    # hash map based on the keyspace
    def __init__(self):
        self.N = 2069
        self.arr: [Bucket] = [Bucket()] * self.N

    def get_hash(self, key):
        return key % self.N

    def put(self, key, value):
        self.arr[self.get_hash(key)].update(key, value)

    def get(self, key):
        return self.arr[self.get_hash(key)].get(key)

    def remove(self, key):
        self.arr[self.get_hash(key)].remove(key)

inp1 = ["DesignHashMap", "put", "get"]
inp2 = [[], [15, 250], [15]]

b = Bucket()
b.update(1, 5)
b.update(2, 5)
b.update(10, 5)
b.update(5, 5)
b.update(5, 10)
b.remove(5)
b.remove(1)
print(b.get(2))
print(b.get(1))

print(b)
