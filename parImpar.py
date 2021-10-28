from random import randint
c = int(0)
soma = int
nDigitado = int
result = str
continuar = str("s")
while(continuar=="s"):
    nDigitado = int(input("Digite um número: "))
    pi = input("Par ou Impar?[p/i]")
    nSorteado = int(randint(1, 10))
    soma = nDigitado + nSorteado
    if (soma%2==0 and pi=="p"):
        c+=1
        continuar = "s"
        print(f"Voce jogou {nDigitado} e o computador {nSorteado}. Total de {soma}, deu PAR\nVocê ganhou!\n\nVamos jogar novamente...")
    if (soma%2!=0 and pi=="i"):
        c+=1
        continuar = "s"
        print(f"Voce jogou {nDigitado} e o computador {nSorteado}. Total de {soma}, deu ÍMPAR\nVocê ganhou!\n\nVamos jogar novamente...")
    if (soma%2==0 and pi=="i"):
        continuar = "n"
        print(f"Voce jogou {nDigitado} e o computador {nSorteado}. Total de {soma}, deu PAR\nVocê perdeu!")
    if (soma%2!=0 and pi=="p"):
        continuar = "n"
        print(f"Voce jogou {nDigitado} e o computador {nSorteado}. Total de {soma}, deu ÍMPAR\nVocê perdeu!")
print(f"\n\nVocê ganhou {c} vezes.")