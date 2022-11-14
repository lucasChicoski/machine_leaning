from animals_classification import Classification  # Importação de módulo

# Introdução a classificação usando machine learning

# gordinho, perna curta, auau


def main():
    classification = Classification(
        arrayAnimal=[[1, 1, 1], [1, 0, 0], [0, 0, 1]], marcacao_teste=[-1, 1, -1])

    classification.startClassification()
    classification.calculandoTaxaDeAcertos()


if __name__ == "__main__":
    main()
