def trocaPalavra():
    str = "Frase simulacao."
    palavraPTrocar = input("Digite a palavra que sera trocada: ")
    palavraNova = input("Digite a palavra que desejar por no lugar: ")
    print(str.replace(palavraPTrocar, palavraNova))


trocaPalavra()