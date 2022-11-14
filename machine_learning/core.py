from sklearn.naive_bayes import MultinomialNB

# lib - sklearn

# sumário

# 1 - verdadeiro , 0 - falso
# 1 - Porco , -1 Cachorro

class Classification:
    def __init__(self, arrayAnimal):
        self.porco1 = [1, 1, 0]
        self.porco2 = [1, 1, 0]
        self.porco3 = [1, 1, 0]
        self.cachorro1 = [1, 1, 1]
        self.cachorro2 = [0, 1, 1]
        self.cachorro3 = [0, 1, 1]

        self.dados = [
            self.porco1,
            self.porco2,
            self.porco3,
            self.cachorro1,
            self.cachorro2,
            self.cachorro3,
        ]

        self.marcacao = [1, 1, 1, -1, -1, -1]

        self.modelo = MultinomialNB()

        self.arrayAnimal = arrayAnimal
        pass

    def trainingClassification(self):
        self.modelo.fit(self.dados, self.marcacao)
        pass

    def startClassification(self):
        self.trainingClassification()

        misteryAnimals = []

        for animal in self.arrayAnimal:
            misteryAnimals.append(animal)
            pass

        resultado = self.modelo.predict(misteryAnimals)

        for index, animal in enumerate(resultado):
            if(animal == -1):
                print("Animal {}".format(index), "É um Cachorro")
                pass
            else:
                print("Animal {}".format(index), "É um Porco")
