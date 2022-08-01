print("")
print("Selecione o número da operação desejada:")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

print("")

opcao = input("Digite sua opção: (1/2/3/4): ")

if (opcao == '1'):
    print("")
    primeiro_numero = int(input("Digite o primeiro número: "))
    print("")
    segundo_numero = int(input("Digite o segundo número: "))
    total = primeiro_numero + segundo_numero
    print("")
    print(primeiro_numero, "+", segundo_numero, "=", total)

if (opcao == '2'):
    print("")
    primeiro_numero = int(input("Digite o primeiro número: "))
    print("")
    segundo_numero = int(input("Digite o segundo número: "))
    total = primeiro_numero - segundo_numero
    print("")
    print(primeiro_numero, "-", segundo_numero, "=", total)

if (opcao == '3'):
    print("")
    primeiro_numero = int(input("Digite o primeiro número: "))
    print("")
    segundo_numero = int(input("Digite o segundo número: "))
    total = primeiro_numero * segundo_numero
    print("")
    print(primeiro_numero, "x", segundo_numero, "=", total)

if (opcao == '4'):
    print("")
    primeiro_numero = int(input("Digite o primeiro número: "))
    print("")
    segundo_numero = int(input("Digite o segundo número: "))
    total = primeiro_numero / segundo_numero
    if (total == int(total)):
        print("")
        print(primeiro_numero, "/", segundo_numero, "=", total)

    else: 
        print("")
        print("Opção inválida!!!")

