from common_data import descriptors, measures, preparations, special_descriptors, ignore_words
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

        print('ingredient', self.raw, 'with name', self.name, 'and quantity', self.quantity, self.measure, 'and descriptor', self.descriptors, 'and preps', self.preparations)

    def _parse_ingredient(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            self.raw = self.raw.replace(char, '')
        if 'to taste' in self.raw:
            self.quantity = 'to taste'
            self.measure = ''
            self.raw.replace('to taste', '')
            self.raw.strip()

        for sd in special_descriptors:
            if sd in self.raw:
                self.descriptors.append(sd)
                self.raw.replace(sd, '')
                self.raw.strip()

        tokens = self.raw.split(' ')

        skip = False
        quantity_is_set = False
        measure_is_set = False
        for t, token in enumerate(tokens):
            if skip:
                skip = False
                continue

            if token in ignore_words:
                continue
            elif self._is_number(token):
                if quantity_is_set:
                    if measure_is_set:
                        self.measure += ' ' + token
                    else:
                        self.measure = token
                        measure_is_set = True
                else:
                    self.quantity, skip = self._match_quantity(t, tokens)
                    quantity_is_set = True
                continue
            elif token in measures:
                if measure_is_set:
                    self.measure += ' ' + token
                else:
                    self.measure = measures[token]
                    measure_is_set = True
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
        i = 1
        # raise NotImplementedError

    def _parse_methods(self):
        # raise NotImplementedError
        i = 1
    def _parse_cuisines(self):
        # raise NotImplementedError
        i = 1

    @staticmethod
    def _is_number(token):
        # returns true if the input is a number (including decimal numbers, fractions, and mixed numbers)
        if len(token) < 1:
            return False
        number_re = re.compile('([0-9]+[ ])?[0-9]*[.]*[/]*[0-9]+')
        result = number_re.search(token)
        if result:
            result = result.string[result.start():result.end()]
        if result == token:
            return True
        else:
            return False

    @staticmethod
    def _match_quantity(t, tokens):
        one_number = tokens[t]
        two_numbers = tokens[t] + ' ' + tokens[t + 1]
        if Ingredient._is_number(two_numbers) and '/' in tokens[t + 1]:
            return Ingredient._mixed_to_float(two_numbers), True
        else:
            return Ingredient._frac_to_float(one_number), False

    @staticmethod
    def _mixed_to_float(mixed):
        mixed = mixed.split()
        decimal = Ingredient._frac_to_float(mixed[1])
        decimal += float(mixed[0])
        return decimal

    @staticmethod
    def _frac_to_float(frac):
        if '/' in frac:
            frac = frac.split('/')
            decimal = float(frac[0]) / float(frac[1])
            return decimal
        else:
            return float(frac)