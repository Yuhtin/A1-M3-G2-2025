disciplinas = {"Algoritimos", "Matematica Discreta", "Python Basico", "Python Basico"}
disciplinas_eletivas = {"Python Avançado", "Visao Computacional"}

print('Disciplinas')
print(disciplinas)

carga_horaria = {
    'Algoritimos': 60,
    'Matematica Discreta': 80,
    'Python Basico': 120,
    'Python Avançado': 50,
    'Visao Computacional': 30
}

print("\nCarga horaria das disciplinas: ")

for disciplina, carga in carga_horaria.items():
    print(f"{disciplina}: {carga}h")

total = sum([carga_horaria[disciplina] for disciplina in disciplinas if disciplina in carga_horaria])
print(f"\nTotal de carga horaria cursada: {total}h")

disciplinas_sem_duplicacao = list(set(disciplinas))
print(f"\nDisciplinas sem duplicação: {disciplinas_sem_duplicacao}")

nova_disciplina = "Python Avançado"
disciplinas.add(nova_disciplina)
print(f"\nNova disciplina adicionada: {nova_disciplina}")
print(f"Disciplinas atualizadas: {disciplinas}")

consulta = "IA Generativa"
if consulta in disciplinas:
    print(f"\nA disciplina {consulta} está na lista.")
else:
    print(f"\nA disciplina {consulta} não está na lista.")