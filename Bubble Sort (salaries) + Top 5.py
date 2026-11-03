def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

sal = [45000.5, 32000.0, 78000.75, 25000.0, 56000.0, 91000.25, 41000.0]
bubble_sort(sal)
print("Sorted salaries:", sal)
print("Top five salaries:", sal[::-1][:5])