import random

caracteres = "abcdefg1234567"

senha = ""

tamanho = int(input("Quantos caracteres terá na senha? "))

for i in range (tamanho):
	senha = senha + random.choice(caracteres)
	
print(f"senha gerada: {senha}")