from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in list(range(30):
        product =  Product(names=(sample(ADJECTIVES, k=1) + sample(NOUNS, k=1))

        for i in list(range(randint(0, 4))):
            product.name

        for j in list(range(randint(0, 4))):
            product.name

        for k in list(range(randint(0, 4))):
            product.name

        for l in list(range(randint(0, 4))):
            product.name

        products.append(product)
    # TODO - your code! Generate and add random products.
    return products


def inventory_report(products):
    name = set()
    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    flammability = random.uniform(0.0, 2.5)
      # TODO - your code! Loop over the products to calculate the report.
    for product in products:
        name.add(product.name)




if __name__ == '__main__':
    inventory_report(generate_products())
