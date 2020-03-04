import fractions

from common_data import descriptors, measures, preparations, special_descriptors


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

    def _parse_ingredient(self):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            self.raw.replace(char, '')

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

        self.name.trim()

    @staticmethod
    def _is_number(token):
        return token[0].isnumeric()

    @staticmethod
    def _match_quantity(t, tokens):
        # the current token is a fraction, won't need to skip
        if '/' in tokens[t]:
            fraction_obj = sum(map(fractions.Fraction, tokens[t]))
            return float(fraction_obj), False

        # there is no next token
        if t + 1 not in range(len(tokens)):
            try:
                fraction_obj = sum(map(fractions.Fraction, tokens[t]))
                return float(fraction_obj), False
            except:
                return 1, False

        # not a mixed number quantity
        if '/' not in tokens[t+1]:
            fraction_obj = sum(map(fractions.Fraction, tokens[t]))
            return float(fraction_obj), False

        # must be a mixed number, skip next token
        try:
            fraction_obj = sum(map(fractions.Fraction, f'{tokens[t]} {tokens[t+1]}'))
            return float(fraction_obj), True
        except:
            try:
                fraction_obj = sum(map(fractions.Fraction, f'{tokens[t]}'))
                return float(fraction_obj), True
            except:
                return 1, True
