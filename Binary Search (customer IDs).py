def binary_search(a, key):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

ids = [3320, 1045, 2301, 1500, 1789]
ids.sort()
print("Sorted IDs:", ids)
key = int(input("Enter account ID to search: "))
pos = binary_search(ids, key)
if pos != -1:
    print("Account ID", key, "found at index", pos)
else:
    print("Account ID", key, "not found")