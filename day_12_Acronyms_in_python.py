#request for a sentence

user_input =str(input("Enter a sentence: "))
text = user_input.split()

Acronyms = " "
for i in text:
    Acronyms = Acronyms +str(i[0]).upper()
print(Acronyms)

#enter the text : My name is Ankit
#Output : MNIA