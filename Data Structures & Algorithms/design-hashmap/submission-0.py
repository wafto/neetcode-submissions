class MyHashMap:
    def __init__(self):
        self.items = [None] * (1 + 10 ** 6)

    def put(self, key: int, value: int) -> None:
        self.items[key] = value        

    def get(self, key: int) -> int:
        value = self.items[key]
        return -1 if value is None else value

    def remove(self, key: int) -> None:
        self.items[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)