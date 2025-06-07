while True:
    # Loop para validar o primeiro número
    while True:
        try:
            fn = input("Enter the first number (or type 'exit' to quit): ")
            if fn.lower() == "exit":
                break
            fn = float(fn)
            break  # Entrada válida
        except ValueError:
            print("Enter a valid number or 'exit' to end program execution...")
    if fn == "exit":
        break  # Sai do programa principal

    # Loop para validar o segundo número
    while True:
        try:
            sn = input("Enter the second number (or type 'exit' to quit): ")
            if sn.lower() == "exit":
                break
            sn = float(sn)
            break  # Entrada válida
        except ValueError:
            print("Enter a valid number or 'exit' to end program execution...")
    if sn == "exit":
        break  # Sai do programa principal

    # Loop para validar o operador
    while True:
        try:
            op = input("Enter a math operator (+, -, /, *, **, %): ")
            if op.lower() == "exit":
                break
            if op in ['+', '-', '/', '*', '**', '%']:
                break  # Operador válido
            else:
                print("Invalid operator. Please enter one of +, -, *, /, %, **.")
        except Exception:
            print("Unexpected error. Please try again.")
    if op == "exit":
        break  # Sai do programa principal

    # Realiza o cálculo
    try:
        if op == '+':
            result = fn + sn
        elif op == '-':
            result = fn - sn
        elif op == '*':
            result = fn * sn
        elif op == '/':
            if sn == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = fn / sn
        elif op == '**':
            result = fn ** sn
        elif op == '%':
            if sn == 0:
                print("Error: Modulo by zero is not allowed.")
                continue
            result = fn % sn
        print(f"The result of {fn} {op} {sn} is {result}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
