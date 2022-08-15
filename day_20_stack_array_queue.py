#Use list as stack, array, and queue

#as a list
l = [3,4]
l += [5,6]
print("After adding new value in list", l)

print(l)

#as a stack
l.append(10)
print("After append", l)
l.pop(0)
print("After popping",l)

#as a queue
l.insert(0, 51)
print(l)
l.pop(0)
print(l)
