from ingredient import Ingredient

class Step:
    def __init__(self, ingredient=None):
        if ingredient is None:
            raise ValueError('Ingredient must be initialized with the ingredient string')

        self.ingredients = []
        self.tools = []
        self.methods = []

        ingredient = Ingredient(ingredient)
        # fill data members
        self._parse_ingredients()
        self._parse_tools()
        self._parse_methods()
        print(ingredient)
        print(ingredient.__dict__)
        print( )

    def _parse_ingredient(self):
        raise NotImplementedError

    def _parse_tools(self):
        raise NotImplementedError

    def _parse_methods(self):
        raise NotImplementedError

    def _parse_cuisines(self):
        raise NotImplementedError