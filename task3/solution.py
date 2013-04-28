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

    def get_sisters(self):
        sisters = []
        for parent in [self.father, self.mother]:
            if isinstance(parent, Person):
                sisters += list(
                    filter(lambda child: child.gender == 'F' and child != self,
                           parent.kids))
        return list(set(sisters))

    def get_brothers(self):
        brothers = []
        for parent in [self.father, self.mother]:
            if isinstance(parent, Person):
                brothers += list(
                    filter(lambda child: child.gender == 'M' and child != self,
                           parent.kids))
        return list(set(brothers))

    def children(self, gender=None):
        if gender is not None:
            return list(filter(lambda child: child.gender == gender,
                               self.kids))
        return self.kids

    def is_direct_successor(self, successor):
        if successor in self.kids:
            return True
        return False
