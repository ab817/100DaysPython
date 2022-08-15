#check if two strings are anagrams

def is_anagrams(s1, s2):
    return set(s1) == set(s2)

#print(is_anagrams('spar','rasp')) #True

s1 = input("Enter the first string ")
print(s1)

s2 = input("Enter the second string")
print(s2)

print(is_anagrams(s1, s2))

#input first string : Ankit
#input second string: Bhattarai
#output : False

#a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.