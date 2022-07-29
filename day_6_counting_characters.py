#make a function that counts characters

def count_characters(s):
    count = {}   #to count occurence of characters
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

word = input("Enter your string: ") #input the data
print(count_characters(word))