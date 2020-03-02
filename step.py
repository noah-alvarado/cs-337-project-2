from ingredient import Ingredient
from common_data import descriptors, measures, preparations, special_descriptors
import re

class Step:
    def __init__(self, raw_step=None, recipe_ingredients=[]):
        self.recipe_ingredients = recipe_ingredients
        if raw_step is None:
            raise ValueError('Ingredient must be initialized with the ingredient string')

        self.raw = raw_step
        self.tools = []
        self.methods = []
        self.ingredients = []

        # fill data members
        self._parse_ingredients()
        self._parse_tools()
        self._parse_methods()
        print(self.ingredients)
        print()

    def _parse_ingredients(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            self.raw = self.raw.replace(char, '')

        for ingredient in self.recipe_ingredients:
            if ingredient.name in self.raw:
                if ingredient.name not in self.ingredients:
                    self.ingredients.append(ingredient)

    def _parse_tools(self):
        # raise NotImplementedError
        print()

    def _parse_methods(self):
        # raise NotImplementedError
        print()

    def _parse_cuisines(self):
        # raise NotImplementedError
        print()