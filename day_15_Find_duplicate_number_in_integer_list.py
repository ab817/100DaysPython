#Find duplicate number in integer list

def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

elements = [3, 4,4, 5,4,6,6]
e = find_duplicates(elements)

print(e)