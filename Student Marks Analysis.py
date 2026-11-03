def average(m):
    p = [x for x in m if x != -1]
    return sum(p) / len(p)

def high_low(m):
    p = [x for x in m if x != -1]
    return max(p), min(p)

def absent(m):
    return m.count(-1)

def mode(m):
    p = [x for x in m if x != -1]
    return max(set(p), key=p.count)

n = int(input("Enter number of students: "))
marks = list(map(int, input("Enter marks (-1 for absent): ").split()))

print("Average score:", average(marks))
h, l = high_low(marks)
print("Highest:", h, " Lowest:", l)
print("Absent students:", absent(marks))
m = mode(marks)
print("Mark with highest frequency:", m, "(", marks.count(m), "times )")