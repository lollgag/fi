class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ChainedHashTableWithReplacement:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair.key == key:
                self.table[index][i] = KeyValuePair(key, value)
                return
        self.table[index].append(KeyValuePair(key, value))

    def find(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair.key == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found")

    def display(self):
        for i, slot in enumerate(self.table):
            print(f"Slot {i}: ", end="")
            for pair in slot:
                print(f"({pair.key}, {pair.value})", end=" -> ")
            print("None")

class ChainedHashTableWithoutReplacement:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                raise KeyError("Duplicate key found")
        self.table[index].append(KeyValuePair(key, value))

    def find(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair.key == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found")

    def display(self):
        for i, slot in enumerate(self.table):
            print(f"Slot {i}: ", end="")
            for pair in slot:
                print(f"({pair.key}, {pair.value})", end=" -> ")
            print("None")

def main():
    size = int(input("Enter the size of the hash table: "))
    print("\nSelect method of chaining:")
    print("1. Chaining with replacement")
    print("2. Chaining without replacement")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        hash_table = ChainedHashTableWithReplacement(size)
    elif choice == '2':
        hash_table = ChainedHashTableWithoutReplacement(size)
    else:
        print("Invalid choice! Exiting...")
        return

    while True:
        print("\nOptions:")
        print("1. Insert a key-value pair")
        print("2. Find a value by key")
        print("3. Delete a key-value pair")
        print("4. Display hash table")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            try:
                hash_table.insert(key, value)
                print("Key-value pair inserted successfully!")
            except KeyError as e:
                print(e)
        elif choice == '2':
            key = input("Enter key to find its value: ")
            value = hash_table.find(key)
            if value is not None:
                print("Value:", value)
            else:
                print("Key not found!")
        elif choice == '3':
            key = input("Enter key to delete: ")
            try:
                hash_table.delete(key)
                print("Key-value pair deleted successfully!")
            except KeyError as e:
                print(e)
        elif choice == '4':
            hash_table.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
