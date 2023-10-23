#faça um programa que leia 3 numeros e veja qual é o maior

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
n3 = float(input("digite o terceiro numero: "))
if n1 > n2 and n1 > n3:
    print("o numero maior é:", n1)
elif n2 > n1 and n2 > n3:
     print("o numero maior é:", n2)
elif n3 > n1 and n3 > n2:
     print("o numero maior é:", n3)

