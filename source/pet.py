
"""
This is documentation for Pet class.
"""

import random

class Pet(object):
    """
    This class will represent a class for pet
    """

    version = '0.1'

    def __init__(self, name, owner):
        """
        creates the variables associated with the class
        :type name: string
        :param name: the name of the pet
        
        :type owner: string
        :param owner: the owner of the pet
        """

        self.name = []
        self.owner = owner
        self.name.append(name)

    def add_pet(self, name):
        """
        adds a pet to the pet list
        :type name: string
        :param name: pet name to add to the list
        """

        self.name.append(name)

    def show_pets(self):
        """
        prints out all the pets in the list
        """

        print ("The owner of these pets are: " + self.owner)
        for each in self.name:
            print (each)

    @classmethod            # alternative constructor
    def random_pets(cls, owner):
        """
        special method was created after to address owners that did not 
        want to pick a pet name.
        :type cls: Pets
        :param cls: an instance of the class passed to __init__
        :type owner: string
        :param owner: the owner of this pet
        """

        pets_random = ['Cocoa', 'Jasper', 'Elmo', 'Chester', 'Rufus']
        random_pet_name = random.choice(pets_random)
        return cls(random_pet_name, owner)

    @staticmethod           # attach a method doesn't need self
    def get_average_age(pet_type):
        """
        prints out the average age of a pet
        :type pet_type: string
        :param pet_type: 3 most popular pets
         """

        if pet_type is 'dog':
            print ('Dogs average life is: 13 years')
        if pet_type is 'cat':
            print ('Cats average life is: 15 years')
        if pet_type is 'fish':
           print ('Gold Fish average life is: 30 years')


if __name__ == "__main__":
    # the first class
    p1 = Pets('jabba', 'Dan Sheffner')
    print(type(p1))
    p1.show_pets()
    print ()
    p1.get_average_age('cat')

    print ()

    # the second class
    p2 = Pets.random_pets('Chris Sheffner')
    print(type(p2))
    p2.show_pets()
    print ()

   # owner gets another pet later on and names it roo
    print ('owner buys another pet later on...')
    p2.add_pet('Roo')
    p2.show_pets()
    print ()

    p2.get_average_age('dog')
    p2.get_average_age('fish')