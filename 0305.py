def fn(start, stop=None, step=1):
    if not stop:
        stop, start = start, 0
    list1 = []
    while start < stop:
        list1.append(start)
        start += step
    return list1

print fn(5) #[0, 1, 2, 3, 4]
print fn(2,5) #[2, 3, 4]
print fn(2, 8, 3) #[2, 5]