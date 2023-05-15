import random

repetir = "S" 
while repetir == "S":
   
    jogo = ["PEDRA", "PAPEL", "TESOURA"]

    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").upper()
    escolha_comput = random.choice(jogo)
    
    while escolha_usuario not in jogo:
        print("Escolha inválida! Você precisa escolher \"pedra, papel ou tesoura!\"")
        escolha_usuario = input("Escolha pedra, papel ou tesoura: ").upper()

    if escolha_usuario == escolha_comput:
        print("Escolhemos a mesma opção: {}".format(escolha_comput))
    else:
        print("Eu escolhi {}, escolhemos diferente ;(".format(escolha_comput))


    repetir= input("Quer jogar novamente? (S ou N): ").upper()
    while repetir not in ["S", "N"]:
        print("Opção inválida, tente novamente")
        repetir = input("Quer jogar novamente? (S ou N): ").upper()
    if repetir == "N":
        print("Fim do jogo, volte sempre!")