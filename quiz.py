print("Seja muito bem vindo ao quiz do Gustavo!") 

answer_user = input("Quer começar? (S/N) ") # Espera o usuário pressionar Enter. A variável answer_user recebe a resposta do usuário.

if answer_user.lower() not in ["s", "S"]:   # Se a resposta do usuário for diferente de "S" ou "s", o programa exibe a mensagem "Até a próxima!".
    quit("Até a próxima!")                  # Encerra o programa.

score = 0                                   # Inicializa a variável score com o valor 0.

print("Começando...")

print("Pergunta 1: Quem desenvolveu o jogo Grand Theft Auto V? \n (a) Rockstar Games \n (b) Ubisoft \n (c) Activision \n (d) EA \n") 
answer_1 = input("Resposta: ") 

if answer_1.lower() == "a":                # Se a resposta do usuário for "a" ou "A", o programa exibe a mensagem "Resposta correta!".
    print("Resposta correta!\n")
    score += 1                             # Incrementa a variável score em 1.
else:                                      # Se a resposta do usuário for diferente de "a" ou "A", o programa exibe a mensagem "Resposta incorreta!".
    print("Resposta incorreta!\n")

print("Pergunta 2: Quem é o ator que interpreta o personagem Tony Stark (Homem de Ferro) nos filmes da Marvel? \n (a) Robert Downey Jr. \n (b) Chris Hemsworth \n (c) Chris Evans \n (d) Mark Ruffalo \n")
answer_2 = input("Resposta: ") 

if answer_2.lower() == "a": 
    print("Resposta correta!\n")
    score += 1
else:                        
    print("Resposta incorreta!\n")

print("Pergunta 3: Quem é o atual camisa 10 do Flamengo? \n (a) Gabigol \n (b) Arrascaeta \n (c) Everton Ribeiro \n (d) Diego \n")
answer_3 = input("Resposta: ")

if answer_3.lower() == "b":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta incorreta!\n")

print(f"O quiz acabou! A sua pontuação é de {score}/3 ponto(s).") # Exibe a pontuação do usuário.