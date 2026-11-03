def binary_search(a, roll):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == roll:
            return True
        elif a[mid] < roll:
            low = mid + 1
        else:
            high = mid - 1
    return False

rolls = list(map(int, input("Enter roll numbers in sorted order: ").split()))
r = int(input("Enter roll number to search: "))
if binary_search(rolls, r):
    print("Roll no", r, "attended the training program")
else:
    print("Roll no", r, "did NOT attend the training program")