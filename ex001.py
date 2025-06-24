import random

def sexo():
    num1 = random.randint(0, 1)
    sexo = ''
    if num1 == 0:
        sexo = 'homen'
        return sexo
    else:
        sexo = 'mulher'
        return sexo

def idade():
    idade = random.randint(15, 90)
    return idade

list = []

for i in range(10):
    list.append({
        "id": i,
        "sexo": sexo(),
        "idade": idade()
    })

print(list)