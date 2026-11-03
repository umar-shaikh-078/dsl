def linear_search(a, roll):
    for i in range(len(a)):
        if a[i] == roll:
            return True
    return False

rolls = list(map(int, input("Enter roll numbers who attended: ").split()))
r = int(input("Enter roll number to search: "))
if linear_search(rolls, r):
    print("Roll no", r, "attended the training program")
else:
    print("Roll no", r, "did NOT attend the training program")