from webscraper import parse_recipe
from step import Step


class Recipe:
    def __init__(self, url):
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.steps = []

        raw_recipe = parse_recipe(url)
        raw_ingredients = raw_recipe['ingredients']
        raw_directions = raw_recipe['directions']
        print (raw_recipe)
        print(raw_ingredients)
        print(raw_directions)
        for direction in raw_directions:
            for sentence in direction.split('.'):
                sentence = sentence.strip()
                if len(sentence) > 0:
                    self.steps.append(Step(sentence))
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
