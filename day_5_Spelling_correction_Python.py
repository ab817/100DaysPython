#pip install textblob
from textblob import TextBlob

def Convert(string):
    li = list(string.split())
    return li

string = input("Enter your word:")
words = Convert(string)
corrected_words =[]
for i in words:
    corrected_words.append(TextBlob(i))

print("Wrong words:", words)
print("Corrected words are:")
for i in corrected_words:
    print(i.correct(), end=" ")
