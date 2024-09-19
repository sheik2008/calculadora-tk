def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

# Menu da calculadora
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Entrada do usuário
escolha = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(f"O resultado é: {adicionar(num1, num2)}")

elif escolha == '2':
    print(f"O resultado é: {subtrair(num1, num2)}")

elif escolha == '3':
    print(f"O resultado é: {multiplicar(num1, num2)}")

elif escolha == '4':
    print(f"O resultado é: {dividir(num1, num2)}")

else:
    print("Opção inválida!")
