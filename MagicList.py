
from Person import Person


class MagicList(Person):

    def __init__(self, *args, **kwargs):
        self.position = []

        Person.__init__(self)

    def __getitem__(self, key) -> int:
        if not self.position or len(self.position) == key:
            self.__setitem__(key)
            return self.position[key]
        elif len(self.position) > key:
            return self.position[key]
        return None

    def __setitem__(self, key):
        if not self.position:
            self.position.append(Person)
        elif len(self.position)-1 >= key:
            self.position[key] = Person

        elif len(self.position) == key and Person != None:
            self.position.append(Person)