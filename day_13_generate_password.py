#Enter the length of password you want to generate
import random

lengthofPassword = int(input("Enter the length of password : "))

#storing letters, numbers and special characters
string="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(string,lengthofPassword ))
print(password)