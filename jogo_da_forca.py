jogando = True
while jogando:
    inicio = "x"
    while inicio != "COMEÇAR":
        inicio = input('Bem-vindo ao jogo da forca, digite "COMEÇAR" para iniciar o jogo.\n').upper()
        if inicio == "COMEÇAR":
            import random
            palavras = ["python","java","javascript","php","sql"]
            palavra = random.choice(palavras).upper()
            acertos = ["_"] * len(palavra)
            erros = 0
            tentativas = 5
            letras_usadas = set()
            print(" ".join(acertos))
            while erros < tentativas and "_" in acertos:
                letra = str(input('\nDigite uma letra ou tente acertar a palavra (SE ERRAR A TENTATIVA DE ESCREVER A PALAVRA, VOCÊ PERDE!).\nCaso queira receber uma dica, digite "DICA":\n'))                    
                if "DICA" in letra.upper():
                    print(" ".join(acertos))
                    print("\nÉ uma linguagem de programação!")
                    continue

                elif len(letra) > 1 and letra.upper() == palavra:
                    break

                elif len (letra) > 1 and letra.upper() != palavra:
                    break  

                if letra in letras_usadas:
                    print("Você ja utilizou essa letra! Tente novamente.")
                    continue

                letras_usadas.add(letra.upper())
                if letra.upper() in palavra:
                    for i in range(len(palavra)):
                        if palavra[i] == letra.upper():
                            acertos[i] = letra.upper()
                else:
                    erros+=1
                    print(f"Letra errada! Tente novamente. ({tentativas - erros} Restantes)")  
                print("Letras usadas:",", ".join(letras_usadas))                    
                print(" ".join(acertos))

            if "_" not in acertos or letra.upper() == palavra:
                    print("Parabéns, você acertou a palavra corretamente!")
            else:
                    print(f"Você perdeu! A palavra era:", palavra.upper())

            continuacao = input('Caso deseje jogar novamente, digite "S", se não digite "N":\n').upper()
            if continuacao == "S":
                continue
            elif continuacao == "N":
                print("Jogo encerrado.")
                jogando = False
        else:
            print('Verifique se está digitando "COMEÇAR" corretamente.')
