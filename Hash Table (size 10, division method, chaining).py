size = 10
table = [[] for _ in range(size)]

def insert(key, value):
    table[key % size].append((key, value))

def search(key):
    for k, v in table[key % size]:
        if k == key:
            return v
    return None

def delete(key):
    h = key % size
    for item in table[h]:
        if item[0] == key:
            table[h].remove(item)
            return True
    return False

def display():
    for i in range(size):
        if table[i]:
            print(i, "->", table[i])

insert(25, "A")
insert(35, "B")
insert(15, "C")
insert(42, "D")
insert(7, "E")
display()

v = search(35)
print("Value for key 35:", v)
v = search(99)
print("Value for key 99:", v if v else "Key not found")

delete(25)
print("After deleting 25:")
display()