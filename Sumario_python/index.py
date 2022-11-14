# alguns comandos python 


#Declaração de variáveis
list2 = []
list = [1, 2, 3, 4, 5, 6, "Lucas"]
nome2 = "lucassssssss"

#Declaração de funções
def teste(algum_numero):
    for element in range(5):
        print(element)

#Loop
for index, element in enumerate(list):
        print(index, element)

#Condicional
if not list:
    print("deu certo")

if not list2:
    print("deu certo")

#Estrutura de dados
config = {
    "name": "Lucas",
    "idade": float(26)
}

##Start de funções
teste("Lucas")

##Imprimindo
print(len(nome2))
print("meu nome é: {}".format("Luycas"), "lasd {}".format("O que é isso <-"))
print(type(config))