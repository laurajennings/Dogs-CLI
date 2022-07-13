class Dog():
    large = [] 
    small = []

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def is_large(self):
        if self.size == "large":
            return True
        

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.name}, {self.size} dog"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.name == other.name and self.size == other.size):
            return True
    
    #It's appropriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()

