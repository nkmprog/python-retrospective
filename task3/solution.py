class Person():
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        self.kids = []
        self.add_child()

    def add_child(self):
        if isinstance(self.father, Person):
            self.father.kids.append(self)

        if isinstance(self.mother, Person):
            self.mother.kids.append(self)

    def _get_siblings(self, gender):
        siblings = []
        for parent in [self.father, self.mother]:
            if isinstance(parent, Person):
                siblings += list(
                    filter(lambda child:
                           child.gender == gender and child != self,
                           parent.kids))
        return list(set(siblings))

    def get_sisters(self):
        return self._get_siblings(gender='F')

    def get_brothers(self):
        return self._get_siblings(gender='M')

    def children(self, gender=None):
        if gender is not None:
            return list(filter(lambda child: child.gender == gender,
                               self.kids))
        return self.kids

    def is_direct_successor(self, successor):
        if successor in self.kids:
            return True
        return False
