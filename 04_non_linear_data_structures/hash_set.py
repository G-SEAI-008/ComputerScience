class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_func(self, key):
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size

        if isinstance(key, int):
            return key % self.size

    def add(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]

        try:
            bucket.remove(key)
        except ValueError:
            pass

    def contains(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        return key in bucket


my_set = HashSet()


my_set.add("Piano")
my_set.add("Running")

my_set.add(2352)

my_set.add(2352)

my_set.add("onaiP")
