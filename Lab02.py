# Calculadora Python simples de autoria própria desenvolvida com os módulos 2 e 3 do curso DSA com 4 funções

print("Selecione o número da operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")
valor = int(input("Digite sua opção (1/2/3/4): "))

entrada1 = int(input("Digite o primeiro número: "))
entrada2 = int(input("Digite o segundo número: "))

if valor == 1:
    entrada1 + entrada2
    print(entrada1, "+", entrada2, "=", entrada1+entrada2)
elif valor == 2:
    entrada1 - entrada2
    print(entrada1, "-", entrada2, "=", entrada1 - entrada2)
elif valor == 3:
    entrada1 * entrada2
    print(entrada1, "x", entrada2, "=", entrada1 * entrada2)
elif valor == 4:
    entrada1 / entrada2
    print(entrada1, "÷", entrada2, "=", entrada1 / entrada2)

else:
    print("Valor inválido, tente novamente")

# Calculadora propositalmente sem tratamento de erro ou retorno ao início
# Mensagem de valor inválido propositalmente após entrada1 e 2
