import os 
def menu():
    print ('calculadora')
    print ('o quer voce quer fazer?')
    print ('[0] soma')
    print ('[1] subtracao')
    print ('[2] multiplicacao')
    print ('[3] divisao')
    print ('[4] novo calculo')
def soma(numero1, numero2): 
    total = numero1 + numero2
    print (total)
    return total

def subtracao(total):
    numero = int(input('numero a subtrair: '))
    total = total - numero
    print (total)
    return total

def multiplicacao(total):
    numero = int(input('numero 2: '))
    total = total * numero 
    print (total)
    return total

def divisao(total):
    numero = int(input('divisor: '))
    if numero == 0:
        print ('erro')
    total = total / numero 
    print (total)
    return total
total = 0
flag = None
while True:
    if flag == None:
        menu()
        escolha = int(input('escolha: '))
        if escolha == 0:
            numero1 = int(input('numero: '))
            numero2 = int(input('numero: '))
            total = soma(numero1, numero2)
            flag = True
        elif escolha == 1:
            total = int(input('numero: '))
            total = subtracao(total)
            flag = True
        elif escolha == 2:
            total = int(input('numero1: '))
            total = multiplicacao(total)
            flag = True
        elif escolha == 3:
            total = int(input('numero: '))
            total = divisao(total)
            flag = True
    else:
        menu()
        escolha = int(input('escolha: '))
        if escolha == 0:
            numero2 = int(input('numero 2: '))
            total = soma(total, numero2)
        elif escolha == 1:
            total = subtracao(total)
        elif escolha == 2:
            total = multiplicacao(total)
        elif escolha == 3:
            total = divisao(total)
        elif escolha == 4:
            flag = None
            total = total * 0
            os.system('cls') 