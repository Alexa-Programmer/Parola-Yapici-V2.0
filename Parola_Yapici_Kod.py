import random

char_pool = "ABCDEFGHIJKLMNOPRSTUVXWYZabcdefghijklmnoprstuvxwyz1234567890@-_*()/\?*!+%"

password = ""

pass_length = "placeholder" # Ya burada tanımlamasaydık

while not pass_length.isdigit():

    pass_length = input("Lütfen şifrenizin kaç karakter uzunluğunda olması gerektiğini yazın: ")

    if not pass_length.isdigit():

        print("Bir sayı girmelisiniz.")

    # neden else kullanıp pass_length'i döngü içinde tam sayıya dönüştürmedik?

    else:

        pass_length = int(pass_length)

# pass_length = int(pass_length)

for i in range(pass_length):

    password = password + random.choice(char_pool)

print("İşte yeni şifreniz: "+password)
