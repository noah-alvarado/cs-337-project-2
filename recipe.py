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

    def __str__(self):
        print_str = 'Here is the recipe:\n\nIngredients:\n'
        for ingredient in self.ingredients:
            if ingredient.quantity_is_set and isinstance(ingredient.quantity, float):
                if ingredient.measure == 'item':
                    description = '\t' + str(ingredient.quantity) + ' '
                else:
                    description = '\t' + str(ingredient.quantity) + ' ' + ingredient.measure
                    if ingredient.quantity > 1:
                        description += 's '
                    else:
                        description += ' '
            else:
                description = '\t'
            remove_comma = False
            for prep in ingredient.preparations:
                if prep not in ingredient.descriptors:
                    description +=  prep + ', '
                    remove_comma = True
            if remove_comma:
                description = description[0:len(description)-2] + ' '
            remove_comma = False
            for descriptor in ingredient.descriptors:
                remove_comma = True
                description += descriptor + ', '
            if remove_comma:
                description = description[0:len(description)-2] + ' '
            description += ingredient.name
            if ingredient.to_taste and ingredient.quantity_is_set:
                description += ' (or to taste)'
            elif ingredient.to_taste:
                description += ' (to taste)'
            print_str += description + '\n'

        print_str += '\nDirections:\n'
        for index, step in enumerate(self.steps):
            print_str += '\tStep:' + str(index + 1) + ': ' + step.raw + '.\n'
        return print_str

    def adjust_portions(self, amount):
        print('Here is the list of changes we are making:')
        saute_preps = ['sear', 'brown', 'saute']
        not_adjusted_list = []
        for ingredient in self.ingredients:
            adjusted = False
            for prep in saute_preps:
                for step in self.steps:
                    if ingredient in step.ingredients and prep in step.methods and ingredient.name in oily_ingredients:
                        if amount < 1.0:
                            if not adjusted:
                                adjusted = True
                                print('\tBecause of the', prep, 'method, we are using', 1.5 * amount, 'times the amount of', ingredient.name)
                                ingredient.quantity *= 1.5 * amount
                        else:
                            if not adjusted:
                                adjusted = True
                                print('\tBecause of the', prep, 'method, we are using', 0.75 * amount, 'times the amount of', ingredient.name)
                                ingredient.quantity *= amount * .75
            if not adjusted:
                not_adjusted_list.append(ingredient.name)
                ingredient.quantity *= amount
                adjusted = True
        if len(not_adjusted_list) > 0:
            print('\tWe will be using ' + str(amount) + ' times the amount of ' + ', and '.join(', '.join(not_adjusted_list).rsplit(', ', 1)) + '.')

        adjusted_steps = []
        for index, step in enumerate(self.steps):
            if len(step.current_time_string) > 0 and step.time_in_minutes > 0:
                if amount >= 1:
                    new_time = step.time_in_minutes + step.time_in_minutes * (amount - 1) * .5
                else:
                    # some math so that doubling and halfing a recipe brings you back to the starting point ;)
                    new_time = step.time_in_minutes / (1 + ((1/amount) - 1) * .5)
                step.time_in_minutes = new_time
                if step.current_time_string in step.raw:
                    adjusted_steps.append('step ' + str(index + 1))
                    #print('In step', index + 1, 'we will go for', str(100*(amount - 1)/2) + '% more time')
                    #print('In step', index + 1, 'we will go for', str(100*(1-(1/(1 + ((1/amount) - 1) * .5)))), '% less time')
                    step.raw = step.raw.replace(step.current_time_string, str(int(step.time_in_minutes)) + ' minutes')
                    step.current_time_string = str(int(step.time_in_minutes)) + ' minutes'
        if len(adjusted_steps) > 0:
            if amount > 1:
                print('\tWe will go for ' + str(100*(amount - 1)/2) + '% more time in ' + ', and '.join(', '.join(adjusted_steps).rsplit(', ', 1)) + '.')
            else:
                print('\tWe will go for ' + str(100*(1-(1/(1 + ((1/amount) - 1) * .5)))) + '% less time in ' + ', and '.join(', '.join(adjusted_steps).rsplit(', ', 1)) + '.')


    def vegify(self):
        raise NotImplementedError

    def meatify(self):
        raise NotImplementedError

    def to_cuisine(self, cuisine):
        raise NotImplementedError
