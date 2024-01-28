class Cliente:

    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        print("Chamando @Property nome()")
        return self.__name.title()

    @name.setter
    def name(self, name):
        print("chamando setter name()")
        self.__name = name