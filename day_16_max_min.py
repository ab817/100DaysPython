#find max and min in unsorted list

l = [3, 2, -1, 24, 78, 65, 24, 23, 0, 1]
print(max(l))
print(min(l))

sum = 0
for x in l:
    sum= sum + x

avg = sum/ len(l)

print("Average",avg)