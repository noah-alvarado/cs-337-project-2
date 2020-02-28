from common_data import measures


class Ingredient:
    def __init__(self, ingredient=None):
        if ingredient is None:
            raise ValueError('Ingredient must be initialized with the ingredient string')

        self.name = '%name%'
        self.quantity = '%quantity%'
        self.measure = '%measure%'

        self.descriptors = []
        self.preparations = []
        self.cuisines = []

    def _parse_ingredient(self, raw):
        bad_chars = ['(', ')', ',']
        for char in bad_chars:
            raw.replace(char, '')

        tokens = raw.split(' ')

        if 'to taste' in raw.lower():
            self.quantity = 'to taste'
            self.measure = ''

        for t, token in enumerate(tokens):
            if self._is_number(token):
                fraction_pos = self._matched_fraction(t, tokens)
            elif token in measures:
                self.measure = measures[token]
            elif token.lower() in measures:
                self.measure = measures[token.lower()]

    @staticmethod
    def _is_number(token):
        raise NotImplementedError

    @staticmethod
    def _matched_fraction(t, tokens):
        raise NotImplementedError
