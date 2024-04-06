import random
characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length=int(input("Şifren kaç haneli olsun?"))
password= ""

for i in range(password_length):
    character= random.choice(characters)

    password += character

print ("işte şifren")
print(password)

