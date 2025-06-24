pessoas = [{'id': 0, 'sexo': 'homem', 'idade': 51}, {'id': 1, 'sexo': 'homem', 'idade': 55}, {'id': 2, 'sexo': 'homem', 'idade': 15}, {'id': 3, 'sexo': 'mulher', 'idade': 55}, {'id': 4, 'sexo': 'homem', 'idade': 83}, {'id': 5, 'sexo': 'homem', 'idade': 44}, {'id': 6, 'sexo': 'mulher', 'idade': 84}, {'id': 7, 'sexo': 'homem', 'idade': 57}, {'id': 8, 'sexo': 'mulher', 'idade': 56}, {'id': 9, 'sexo': 'mulher', 'idade': 46}]

total_idade = 0
total_pessoas = len(pessoas)
total_homens = 0
total_mulheres = 0

for pessoa in pessoas:
    total_idade += pessoa['idade']
    if pessoa['sexo'] == 'homem':
        total_homens += 1
    elif pessoa['sexo'] == 'mulher':
        total_mulheres += 1

media_idade = total_idade / total_pessoas
porcentagem_homens = (total_homens / total_pessoas) * 100
porcentagem_mulheres = (total_mulheres / total_pessoas) * 100

print(f"Média de idade: {media_idade:.2f}")
print(f"Homens: {porcentagem_homens:.2f}%")
print(f"Mulheres: {porcentagem_mulheres:.2f}%")
