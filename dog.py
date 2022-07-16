'''Classes.'''
class Dog():
    '''Dog class.'''

    def __init__(self, name, owner, breed, size, age, gender,
                feed_meds, grooming, belongings, friendly):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.size = size
        self.age = age
        self.gender = gender
        self.feed_meds = feed_meds
        self.grooming = grooming
        self.belongings = belongings
        self.friendly = friendly

    def __str__(self):
        return f"""\n{self.name}: \nBelongs to {self.owner}, is a {self.size},
                {self.breed} {self.gender}, {self.age} years old. Special food
                or medication: {self.feed_meds}, Requires grooming: {self.grooming},
                Belongings: {self.belongings}, Friendly: {self.friendly}"""

    def __repr__(self):
        return self.__str__()
