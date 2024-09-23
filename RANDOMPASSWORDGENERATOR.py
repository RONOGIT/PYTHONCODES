import random
import string

def password_generator(length, num):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    for i in range(num):  
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated password {i + 1}: {password}") 


length = int(input("Enter the length of the random password to generate: "))
num = int(input("Enter the number of random passwords to generate: "))
password_generator(length, num)