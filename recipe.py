import random

from ingredient import Ingredient
from webscraper import parse_recipe
from common_data import meat_to_veg, meat_types, veg_to_meat, veg_types


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
        for i in range(len(self.ingredients)):
            for kind, matches in meat_types.items():
                found = None
                for match in matches:
                    if match in self.ingredients[i].name:
                        found = kind
                        break

                if found is None:
                    break

                old = self.ingredients[i].name
                self.ingredients[i].name = random.choice(meat_to_veg[found])
                new = self.ingredients[i].name

                yield old, new
                break

    def meatify(self):
        num_items_replaced = 0
        max_items_replaced = round((3 + (len(self.ingredients) * 0.2)) / 2)

        for i in range(len(self.ingredients)):
            if num_items_replaced > max_items_replaced:
                break

            for kind, matches in veg_types.items():
                found = None
                for match in matches:
                    if match in self.ingredients[i].name:
                        found = kind
                        break

                if found is None:
                    break

                old = self.ingredients[i].name
                self.ingredients[i].name = random.choice(veg_to_meat[found])
                new = self.ingredients[i].name

                num_items_replaced += 1
                yield old, new
                break

        if num_items_replaced:
            # try to guess new meat
            new_ingredient = Ingredient('1/2 lb grilled chicken breast')
            yield None, new_ingredient

    def to_cuisine(self, cuisine):
        raise NotImplementedError
