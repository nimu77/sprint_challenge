# modules/product.py
import random


class Product:
    '''

    '''
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
                 identifier = random.randint(1000000, 9999999)):
                 self.name = name
                 self.price = price
                 self.weight = weight
                 self.flammability = flammability
                 self.identifier = identifier

    def stealability(self):
        stealable = self.price / self.weight

        if stealable < 0.5:
            print("Not so stealable")
        elif stealable >= 0.5 and stealable < 1.0:
            print("Kinda stealable")
        else:
            print("Very stealable")

    def explode(self):
        explodable = self.flammability * self.weight

        if explodable < 10:
            print("...fizzle.")
        elif explodable >= 10 and explodable < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")

class BoxingGlove(Product):
    def __int__(self, name, price = 10, weight = 10, flammability = 0.5,
                 identifier = random.randint(1000000, 9999999)):
                 super().__init__(name=name, price=price, weight=weight,
                 flammability=flammability, identifier=identifier)



    def explode(self):
        print("...it's a glove.")

    def punch(self):
        weight_glove = self.weight

        if weight_glove < 5:
            print("That tickles.")
        elif weight_glove >=5 and weight_glove < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
