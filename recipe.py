from webscraper import parse_recipe


class Recipe:
    def __init__(self, url):
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.steps = []

        raw_ingredients, raw_directions = parse_recipe(url)
        raise NotImplementedError

    def __str__(self):
        print('recipe stuff here')

    def adjust_portions(self, amount):
        raise NotImplementedError

    def vegify(self):
        raise NotImplementedError

    def meatify(self):
        raise NotImplementedError

    def to_cuisine(self, cuisine):
        raise NotImplementedError
