# 🧮 Calculadora Python para Linux

Este é um projeto simples de uma calculadora em Python programada no VSCode que roda em sistemas Linux, criado como parte do curso da EBAC no módulo de Lógica de Programação e Automação de Tarefas com Linux.

---

## 📂 Estrutura do Projeto

- `calculadora.py`: Script Python com a lógica da calculadora.
- `calculadora.sh`: Script shell que executa o script Python.
- `comandos.txt`: Arquivo com os comandos utilizados.

---

## 🚀 Como Executar no Linux

### 1. Clone o repositório

```bash
git clone https://github.com/EnzoTorres3023/calculadora_linux_python_ebac.git
```

### 2. Torne o script `.sh` executável

```bash
chmod 744 calculadora.sh
```

> Isso garante permissões de leitura, escrita e execução para o dono, e apenas leitura para grupo e outros.

### 3. Execute o script

```bash
./calculadora.sh
```

---

## 💡 O que faz cada arquivo

### 1. `calculadora.py`

Contém o código Python com a lógica principal da calculadora:

- Solicita dois números ao usuário
- Valida se a entrada é um número (tratamento de erro com `try/except`)
- Exibe um menu de operações:
  - Soma
  - Subtração
  - Multiplicação
  - Divisão
- Executa a operação escolhida
- Mostra o resultado
- Pergunta se o usuário deseja continuar ou sair

### 2. `calculadora.sh`

É um script shell que executa o código Python automaticamente. Conteúdo do arquivo:

```bash
#!/bin/bash
python3 calculadora.py
```

> Simples e direto: ele chama o interpretador Python e roda o script.

### 3. `comandos.txt`

Contém os comandos usados para:

- Criar os arquivos
- Definir permissões
- Executar o script

Conteúdo:

```
mkdir meus_scripts
cd meus_scripts
nano calculadora.py
nano calculadora.sh
chmod 744 calculadora.sh
./calculadora.sh
```

---

## 🔍 Explicação do código `calculadora.py`

```python
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

    # Condicional para cada operação
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

    # Deseja continuar?
    continuar = input("\nDeseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora. Até logo!")
        break
```

### 🧠 Pontos importantes:

- A calculadora **valida entrada numérica** com `try/except`.
- Usa **estrutura de repetição `while`** para permitir múltiplos cálculos.
- Contém **tratamento de erro para divisão por zero**.
- O menu e a execução são feitos com `if/elif/else`.

---

## 👨‍💻 Autor

Desenvolvido por **Enzo Torres** como parte do curso de **Análise de Dados** da EBAC 🚀
