from webscraper import parse_recipe
from step import Step
from ingredient import Ingredient
from common_data import oily_ingredients


class Recipe:
    def __init__(self, url):
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.steps = []

        raw_recipe = parse_recipe(url)
        raw_ingredients = raw_recipe['ingredients']
        raw_directions = raw_recipe['directions']
        print(raw_ingredients)
        print(raw_directions)
        for ingredient in raw_ingredients:
            processed_ingredient = Ingredient(ingredient)
            self.ingredients.append(processed_ingredient)
            for tool in processed_ingredient.tools:
                if tool not in self.tools:
                    self.tools.append(tool)
        for direction in raw_directions:
            for sentence in direction.split('.'):
                sentence = sentence.strip()
                if len(sentence) > 0:
                    processed_step = Step(sentence, self.ingredients)
                    self.steps.append(processed_step)
                    for tool in processed_step.tools:
                        if tool not in self.tools:
                            self.tools.append(tool)
                    for method in processed_step.methods:
                        if method not in self.methods:
                            self.methods.append(method)
        raise NotImplementedError

    def __str__(self):
        print('recipe stuff here')

    def adjust_portions(self, amount):
        saute_preps = ['sear', 'brown', 'saute']
        for ingredient in self.ingredients:
            adjusted = False
            for prep in saute_preps:
                for step in self.steps:
                    if ingredient in step.ingredients and prep in step.methods and ingredient.name in oily_ingredients:
                        if amount < 1.0:
                            if not adjusted:
                                adjusted = True
                                ingredient.quantity *= 1.5 * amount
                        else:
                            if not adjusted:
                                adjusted = True
                                ingredient.quantity *= amount * .75
            if not adjusted:
                ingredient.quantity *= amount
                adjusted = True

        for step in self.steps:
            if len(step.current_time_string) > 0 and step.time_in_minutes > 0:
                new_time = step.time_in_minutes + step.time_in_minutes * (amount - 1) * .5
                if step.current_time_string in step.raw:
                    step.raw.replace(step.current_time_string, step.time_in_minutes + ' minutes')

    def vegify(self):
        raise NotImplementedError

    def meatify(self):
        raise NotImplementedError

    def to_cuisine(self, cuisine):
        raise NotImplementedError
