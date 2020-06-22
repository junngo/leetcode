from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        val = self.store.pop(key)
        self.store[key] = val

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)

        else:
            if self.capacity > 0:
                self.capacity -= 1

            else:
                self.store.popitem(last=False)

        self.store[key] = value


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    cache = LRUCache(capacity)

    cache.put(1, 1);
    cache.put(2, 2);
    # print(cache.get(1));    # returns 1
    # cache.put(3, 3);        # evicts key 2
    # print(cache.get(2));    # returns -1 (not found)
    # cache.put(4, 4);        # evicts key 1
    # print(cache.get(1));    # returns -1 (not found)
    # print(cache.get(3));    # returns 3
    # print(cache.get(4));    # returns 4

    print(cache.store)
