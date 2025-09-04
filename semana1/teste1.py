def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def div(num1,num2):
    return num1/num2

def mult(num1,num2):
    return num1 * num2





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
            print(f"resultado:{soma(num1,num2)}")
            print("---"*10)

        elif(opcao ==2):
            print("---"*10)
            print(f"resultado:{subtracao(num1,num2)}")
            print("---"*10)

        elif(opcao == 3):
            print("---"*10)
            print(f"resultado:{round(div(num1,num2),2)}")
            print("---"*10)

        elif(opcao == 4):
            print("---"*10)
            print(f"resultado:{mult(num1,num2)}")
            print("---"*10)
    else:
        print("Comando inválido, tente novamente!")

