def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

sal = [45000.5, 32000.0, 78000.75, 25000.0, 56000.0, 91000.25, 41000.0]
selection_sort(sal)
print("Sorted salaries:", sal)
print("Top five salaries:", sal[::-1][:5])