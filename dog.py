class Dog():

    def __init__(self, name, owner, breed, size, age, gender, feed_meds, grooming, belongings, friendly):
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


    #What happens when you pass object to print?
    def __str__(self):
        return f"\n{self.name}: \nBelongs to {self.owner}, is a {self.size}, {self.breed} {self.gender}, {self.age} years old. Special food or medication: {self.feed_meds}, Requires grooming: {self.grooming}, Belongings: {self.belongings}, Friendly: {self.friendly}"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.name == other.name and self.size == other.size):
            return True
    
    #It's appropriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()

