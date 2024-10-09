# Definindo o metodo imc antes de chamá-lo
def imc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado

# Informações da pessoa
nome = 'Pedro'
idade = 23
altura = 1.80
peso = 70

# Exibindo as informações
print('Olá ' + nome + ', a sua idade é ' + str(idade) + ' e sua altura e peso são ' + str(altura) + ', ' + str(peso))

certo = input('Digite (c) para certo e (e) para errado: ')

# Verificando a resposta do usuário
if certo == 'c' or certo == 'C':
    print('Informações confirmadas!')
    resultado_imc = imc(peso, altura)  # Chamando a função imc
    print(f'Seu IMC é: {resultado_imc:.2f}')  # Exibindo o IMC formatado com 2 casas decimais
else:
    print('Informações incorretas')