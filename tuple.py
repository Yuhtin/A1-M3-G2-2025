# Imutável = Não pode ser alterado.
# Ordenada, vai garantir que seja ordenada

tuple_simples = (20, 5, 2, 3, 5)
print(sorted(tuple_simples)) # Printa ordenado

tuple = ((-56.34, -20), (-50, -25), (-23, -21))
print(tuple)

print(tuple.index((-23, -21))) # Retorna index 2

# Desempacotar = tirar variaveis da tupla. 
a, b, c = tuple

print(a) # Retorna (-56.34, -20)
print(b) # Retorna (-50, -25)
print(c) # Retorna (-23, -21)

tamanho = len(tuple)
print(tamanho) # Retorna 3