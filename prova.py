import os
prova=[]
valor = 0 
questao1={
    "valor_questão":"10",
    "enunciado":"Quem surgiu primeiro... O ovo ou a galinha?",
    "op1":"Galinha",
    "op2":"Dinossauro",
    "op3":"Adão",
    "op4":"Ovo"
}

questao2= {
    "valor_questão":"10",
    "enunciado":"Qual a capital da França",
    "op1":"Moçambique",
    "op2":"Osaka",
    "op3":"Paris",
    "op4":"Amsterdã"   
}

questao3={
    "valor_questão":"10",
    "enunciado":"Quem escreveu a peça de teatro 'Romeu e Julieta'?",
    "op1":"William Shakespeare",
    "op2":"Mark Twain",
    "op3":"Charles Dickens",
    "op4":"Jane Austen"
}

questao4={
    "valor_questão":"10",
    "enunciado":"Qual é o maior planeta do sistema solar em termos de tamanho e massa?",
    "op1":"Netuno",
    "op2":"Júpiter",
    "op3":"Marte",
    "op4":"Vênus"
}

questao5={
    "valor_questão":"10",
    "enunciado":"Qual o simbolo quimico para o elemento oxigênio?",
    "op1":"C",
    "op2":"H",
    "op3":"N",
    "op4":"O"
}
prova.append(questao1)
prova.append(questao2)
prova.append(questao3)
prova.append(questao4)
prova.append(questao5)

gabarito=['a','c','a','b','d']
marcacoes=[]

for num,questao in enumerate(prova):
    print(num+1,")",questao["enunciado"])
    print("a)",questao["op1"])
    print("b)",questao["op2"])
    print("c)",questao["op3"])
    print("d)",questao["op4"])
    print("\n")
    marcacoes.append(input("Digite a resposta da letra da resposta escolhida:"))
    os.system('cls')
    
for i in range(0,5):
    if marcacoes[i]==gabarito[i]:
        print("Questão",i+1,"Correta!")
        print("resposta correta:",gabarito[i])
        valor=valor+10
    else:print("Questão",i+1,"Incorreta!")
print("\nVocê tirou:",valor)