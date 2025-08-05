# Tuplas em Python

## Alunos envolvidos

- Davi Duarte
- João Furtado  
- Nicole Neves
- Isabel Montenegro
- Eduardo Casarini
- Christian Santos
- Pedro Siqueira

## O que são Tuplas?

Tuplas são estruturas de dados em Python com duas características principais:

- **Imutáveis**: Não podem ser alteradas após criação
- **Ordenadas**: Mantêm a ordem dos elementos

## Exemplos Práticos

### Tupla Simples

```python
tuple_simples = (20, 5, 2, 3, 5)
print(f'Lista Ordenada: {sorted(tuple_simples)}')
```

### Tupla Aninhada (com coordenadas)

```python
tuple = ((-56.34, -20), (-50, -25), (-23, -21))
print(f'Tupla Aninhada {tuple}')
```

### Operações com Tuplas

#### Encontrar índice de um elemento

```python
print(f'Index: {tuple.index((-23, -21))}')  # Retorna 2
```

#### Desempacotamento

Extrair variáveis da tupla:

```python
a, b, c = tuple
print(f'Primeiro valor: {a}')   # (-56.34, -20)
print(f'Segundo valor: {b}')    # (-50, -25)
print(f'Terceiro valor: {c}')   # (-23, -21)
```

#### Tamanho da tupla

```python
tamanho = len(tuple)
print(f'Tamanho da tupla: {tamanho}')
```

## Quando usar Tuplas?

- Para dados que não devem ser modificados
- Para coordenadas (x, y)
- Para retornar múltiplos valores de uma função
- Quando a ordem dos elementos é importante