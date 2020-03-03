from ingredient import Ingredient
from common_data import descriptors, measures, preparations, special_descriptors, prep_tools, task_tools
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
        self.current_time_string = ''
        self.time_in_minutes = 0

        # fill data members
        self._parse_ingredients()
        self._parse_tools()
        self._parse_methods()
        self._parse_time()

    def _parse_time(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            raw_clean = self.raw.replace(char, '')
        step_words = raw_clean.split()
        for index, word in step_words:
            if Ingredient._is_number(word):
                if step_words[index + 1] == 'hour' or step_words[index + 1] == 'hours':
                    current_time_string = word + step_words[index + 1]
                    time_in_minutes = float(word) * 60
                elif step_words[index + 1] == 'minutes':
                    current_time_string += word + step_words[index + 1]
                    time_in_minutes += float(word)
                elif step_words[index + 1] == 'seconds':
                    current_time_string += word + step_words[index + 1]
                    time_in_minutes += float(word) / 60


    def _parse_ingredients(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            raw_clean = self.raw.replace(char, '')

        for ingredient in self.recipe_ingredients:
            if ingredient.name in raw_clean:
                if ingredient.name not in self.ingredients:
                    self.ingredients.append(ingredient)

    def _parse_tools(self):
        for word, tools in task_tools.items():
            if word in self.raw:
                for tool in tools:
                    if tool not in self.tools:
                        self.tools.append(tool)

    def _parse_methods(self):
        # raise NotImplementedError
        for word, tools in task_tools.items():
            if word in self.raw and word not in self.methods:
                self.methods.append(word)