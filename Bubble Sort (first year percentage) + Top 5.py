def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

per = [78.5, 85.2, 66.0, 92.4, 71.8, 88.0, 59.5, 80.1]
bubble_sort(per)
print("Sorted percentages:", per)
print("Top five scores:", per[::-1][:5])