# Alunos envolvidos:
# Davi Duarte, João Freitas, Nicole Neves, Isabel Montenegro, Eduardo Cassarini, Christian Santos

# Imutável = Não pode ser alterado.
# Ordenada, vai garantir que seja ordenada

tuple_simples = (20, 5, 2, 3, 5)
print(f'Lista Ordenada: {sorted(tuple_simples)}')

tuple = ((-56.34, -20), (-50, -25), (-23, -21))
print(f'Tupla Aninhada {tuple}')

print(f'Index: {tuple.index((-23, -21))}') # Retorna index 2

# Desempacotar = tirar variaveis da tupla. 
a, b, c = tuple

print(f'Primeiro valor da tupla: {a})') # Retorna (-56.34, -20)
print(f'Segundo valor da tupla: {b}') # Retorna (-50, -25)
print(f'Terceiro valor da tupla: {c}') # Retorna (-23, -21)

tamanho = len(tuple)
print(f'Tamanho da tupla: {tamanho}')