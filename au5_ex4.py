nome=input('Qual é o nome?')
maiuscula=nome.upper()
print('Seu nome em letras maiusculas é {}'.format(maiuscula))
minuscula=nome.lower()
print('Seu nome em letras minusculas é {}'.format(minuscula))
sem_espaco=len(nome)-nome.count(' ')
print('Seu nome tem {} letras.'.format(sem_espaco))
primeiro=nome.find(' ')
print('Seu primeiro nome tem {} letras'.format(primeiro))
