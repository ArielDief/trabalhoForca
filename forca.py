#Ariel Diefenthaeler Olivera, RA:1134433
#Eduardo da Silva sichelero, RA:1134933

import sys
from funcoes import os, time, aguarde, limparTela, palavraChave

historico = []
while True:
    desafiante = input("Digite o nome do Desafiante: ")
    competidor = input("Digite o nome do Competidor: ")

    limparTela()
    print(f"{desafiante}, insira as informações para o jogo da forca:\n")
    palavrachave = input("Palavra chave: ")
    dica1 = input("Dica 1: ")
    dica2 = input("Dica 2: ")
    dica3 = input("Dica 3: ")
    limparTela()

    ultimaLetra = set()
    num_erros = 0
    max_erros = 5
    num_dicas = 0
    print(f"{competidor}, você tem {len(palavrachave)} letras para adivinhar.\n")
    
    
    while num_erros < max_erros and len(ultimaLetra) < len(palavrachave):
        palavraChave(palavrachave, ultimaLetra)
        print(f"\nDicas usadas: {num_dicas} / 3 | Erros: {num_erros} / {max_erros}\n")
        palpite = input (
        '''Digite... 
        (1) Para jogar 
        (2) Para solicitar uma dica 
        (3) Para encerrar o programa 
        Quando completar a palavra, digite 1 e pressione duas vezes o enter.
        Opção:''')

        if palpite.lower() == "3":
            print("Programa encerrado, obrigado por jogar.")
            sys.exit()

        elif palpite.lower() == "2":
            if num_dicas >= 3:
                print("Você já usou todas as dicas disponíveis!")
                aguarde()

            else:
                num_dicas += 1
                print(f"Dica {num_dicas}: {dica1 if num_dicas == 1 else dica2 if num_dicas == 2 else dica3}")
                letra = input("Digite uma letra: ")
                if letra in palavrachave:
                    ultimaLetra.add(letra)
                else:
                    num_erros += 1

        elif palpite.lower() == "1":
            letra = input("Digite uma letra: ")
            if letra in ultimaLetra:
                print("Você já tentou essa letra antes!")
                aguarde()
            elif letra in palavrachave:
                ultimaLetra.add(letra)
            else:
                num_erros += 1
        else:
            print("Comando inválido, tente novamente.")
            aguarde()
        limparTela()
    if num_erros == max_erros:
        print("Você perdeu!")
        print(f"A palavra era '{palavrachave}'.")
    else: 
        print("Parabéns, você ganhou!")
        arquivo = open("historico.txt","a")
        arquivo.write("Nome do competidor:"+competidor+"/ Nome do desafiante:"+desafiante+" /palavra: "+ palavrachave +"\n")
        arquivo.close()

    historico.append({
    'Desafiante': desafiante,
    'Competidor': competidor,
    'Palavra chave': palavrachave,
    'Número de dicas usadas': num_dicas,
    'Número de erros': num_erros,
})

    while True:
        jogar_novamente = input('''Digite... 
        (3) Para jogar novamente:
        (4) Para conferir o histórico/salvar jogo:
        (5) Para sair:
        Opção:''')
        if jogar_novamente == "3":
            limparTela()
            break
        limparTela()
        
        if jogar_novamente == "4":
            try:
                arquivo = open("historico.txt","r")
                dados = arquivo.read()
                print(dados)
                arquivo.close()
                retornar = input("Obrigado por jogar, para recomeçar o jogo para pressione 1: ")
            except:
                break
       
        else :
            palpite.lower() == "5"
            print("Programa encerrado, obrigado por jogar.")
            sys.exit()
        