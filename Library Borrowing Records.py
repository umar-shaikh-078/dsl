books = [5, 3, 0, 8, 2, 5, 0, 4]

print("Borrowing Records:", books)
print("Average:", sum(books) / len(books))
print("Highest Borrowing:", max(books))
print("Lowest Borrowing:", min(books))
print("Members with Zero Borrowing:", books.count(0))

from collections import Counter
c = Counter(books)
m = max(c.values())

print("Most Frequent Borrowing:", end=" ")
for k, v in c.items():
    if v == m:
        print(k, end=" ")
print()