def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

per = [78.5, 85.2, 66.0, 92.4, 71.8, 88.0, 59.5, 80.1]
selection_sort(per)
print("Sorted percentages:", per)
print("Top five scores:", per[::-1][:5])