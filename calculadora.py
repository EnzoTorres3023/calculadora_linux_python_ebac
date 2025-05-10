print("Calculadora")

while True:
    # Validação do primeiro número
    while True:
        entrada1 = input("Digite o primeiro número: ")
        try:
            num1 = float(entrada1)
            break
        except ValueError:
            print("⚠️ Valor inválido! Por favor, digite um número.")

    # Validação do segundo número
    while True:
        entrada2 = input("Digite o segundo número: ")
        try:
            num2 = float(entrada2)
            break
        except ValueError:
            print("⚠️ Valor inválido! Por favor, digite um número.")

    # Menu de operações
    print("\nEscolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    opcao = input("Digite o número da operação (1/2/3/4): ")

    # Condicional
    if opcao == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif opcao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("\nErro: divisão por zero não é permitida.")
    else:
        print("\nOpção inválida. Tente novamente.")

    # Continuar?
    continuar = input("\nDeseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora. Até logo!")
        break
