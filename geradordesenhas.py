import string
import random


def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = " ".join(random.choice(characters) for _ in range(lenght))
    return password



lenght = int(input("Digite o tamanho da senha: "))
use_uppercase = input("Incluir letras maiúsculas? (s/n) ").lower() =='s'
use_numbers = input("Incluir números? (s/n)").lower() == 's'
use_symbols = input("Incluir símbolos? (s/n) ").lower() == 's'

generate_password = generate_password (lenght, use_uppercase, use_numbers, use_symbols)

print(f"Sua senha gerada é: {generate_password}")