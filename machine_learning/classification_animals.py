from core import Classification #Importação de módulo

# Introdução a classificação usando machine learning


def main():
    classification = Classification(
        arrayAnimal=[[1, 1, 1], [1, 0, 0], [0, 0, 1]])

    classification.startClassification()


if __name__ == "__main__":
    main()
