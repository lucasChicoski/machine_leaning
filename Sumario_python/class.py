# Introdução à Classe

class TryingClass:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def showingTheName(self):
        print("O nome passado por parâmetro foi: {}".format(self.name))


def main():
    print("hello world")
    theName = TryingClass(name="asd")
    theName.showingTheName()


if __name__ == "__main__":
    main()
