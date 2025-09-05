def soma(n1,n2):
    return round(n1 + n2,2)

def subtracao(n1,n2):
    return round(n1 - n2,2)

def div(n1,n2):
    return round(n1/n2,2)

def mult(n1,n2):
    return round(n1 * n2,2)



historico = []
try:
    while(True):
        print("Calculadora\n Digite 1 para somar \n Digite 2 para subtrair \n Digite 3 para dividir \n Digite 4 para multiplicar \n Digite 0 para saír")
        opcao = float(input("Comando:"))
        
        if (opcao == 0):
            print("Encerrando")
            break
        
        elif ( 1 <= opcao <= 4 ):
            num1 = float(input("Número 1:"))
            num2 = float(input("Número 2:"))

            if (opcao == 1):
                print("---"*10)
                resultado = soma(num1,num2)
                print(f"resultado:{resultado}")
                historico.append(resultado)
                print("---"*10)

            elif(opcao ==2):
                print("---"*10)
                resultado = subtracao(num1,num2)
                print(f"resultado:{resultado}")
                historico.append(resultado)
                print("---"*10)

            elif(opcao == 3):
                print("---"*10)
                resultado = div(num1,num2)
                print(f"resultado:resultado,2)")
                historico.append(resultado)
                print("---"*10)

            elif(opcao == 4):
                print("---"*10)
                resultado = mult(num1,num2)
                print(f"resultado:{resultado}")
                historico.append(resultado)
                print("---"*10)
                
        else:
            print("---"*10)
            print("Comando inválido, tente novamente!")
            print("---"*10)

    print("---"*10)
    print("Histórico de resultados:")
    for i in historico:
        print(i)
    print("---"*10)



except ValueError:
    print("Somente números.")
except ZeroDivisionError:
    print("Não é possivel dividir por 0")
