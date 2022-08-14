#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#This is less like the for keyword in other programming languages, and works more like an iterator method as
# found in other object-orientated programming languages.

learningfor = ['learn', 'for', 'loop']

for x in learningfor:
    print(x)

#for individual words
for y in 'learningfor':
    print(y)

#for a range
for x in range(3, 6):
  print(x)

for x in range(2, 30, 3):    #increment by 3
  print(x)

#nested loops
f_para = ["learn", "python", "for"]
s_para = ["loop", "by", "example"]

for x in f_para:
  for y in s_para:
    print(x, y)