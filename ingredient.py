from common_data import descriptors, measures, preparations, special_descriptors
import re

class Ingredient:
    def __init__(self, ingredient=None):
        if ingredient is None:
            raise ValueError('Ingredient must be initialized with the ingredient string')

        self.raw = ingredient

        self.name = ''
        self.quantity = 1
        self.measure = 'item'

        self.descriptors = []
        self.preparations = []
        self.cuisines = []

        # fill data members
        self._parse_ingredient()
        self._parse_tools()
        self._parse_methods()
        self._parse_cuisines()

    def _parse_ingredient(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            self.raw = self.raw.replace(char, '')
        if 'to taste' in self.raw:
            self.quantity = 'to taste'
            self.measure = ''
            self.raw.replace('to taste', '')
            self.raw.trim()

        for sd in special_descriptors:
            if sd in self.raw:
                self.descriptors.append(sd)
                self.raw.replace(sd, '')
                self.raw.trim()

        tokens = self.raw.split(' ')

        skip = False
        for t, token in enumerate(tokens):
            if skip:
                skip = False
                continue

            if self._is_number(token[0]):
                self.quantity, skip = self._match_quantity(t, tokens)
                continue
            elif token in measures:
                self.measure = measures[token]
                continue
            elif token.lower() in measures:
                self.measure = measures[token.lower()]
                continue
            elif token.lower() in descriptors:
                self.descriptors.append(token.lower())
                continue
            elif token.lower() in preparations:
                self.preparations.append(token.lower())
                continue

            self.name = self.name + token + ' '

        self.name.strip()

    def _parse_tools(self):
        raise NotImplementedError

    def _parse_methods(self):
        raise NotImplementedError

    def _parse_cuisines(self):
        raise NotImplementedError

    @staticmethod
    def _is_number(token):
        # returns true if the input is a number (including decimal numbers, fractions, and mixed numbers)
        number_re = re.compile('([0-9]+[ ])?[0-9]*[.]*[/]*[0-9]+')
        result = number_re.search(token)
        if result:
            result = result.string[result.start():result.end()]
        print('is_number')
        if result == token:
            print(token, ' is a number')
        else:
            print(token, ' is not a number')

    @staticmethod
    def _match_quantity(t, tokens):
        raise NotImplementedError
