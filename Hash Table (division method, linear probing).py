size = 10
table = [None] * size

def insert(key):
    h = key % size
    for i in range(size):
        idx = (h + i) % size
        if table[idx] is None or table[idx] == "DEL":
            table[idx] = key
            return
    print("Table is full")

def search(key):
    h = key % size
    for i in range(size):
        idx = (h + i) % size
        if table[idx] is None:
            return -1
        if table[idx] == key:
            return idx
    return -1

def delete(key):
    idx = search(key)
    if idx != -1:
        table[idx] = "DEL"
        return True
    return False

def display():
    print(table)

for k in [25, 35, 15, 42, 7]:
    insert(k)
display()
print("Key 15 found at index:", search(15))
print("Key 99 found at index:", search(99))
delete(35)
print("After deleting 35:")
display()
print("Key 15 found at index:", search(15))