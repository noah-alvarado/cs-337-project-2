from webscraper import parse_recipe


def print_recipe(recipe):
    return


if __name__ == '__main__':
    url = input('Recipe URL: ')

    # raw_ingredients, raw_directions = parse_recipe(url)

    # setup the shit
    recipe = {
        'ingredients': [],
        'tools': [],
        'methods': [],
        'steps': []
    }

    # loop forever so we can keep performing transformations
    while True:
        # print the recipe
        # print_recipe(recipe)

        # print available transformations
        print('\nAvailable transformations:')

        print('\tAdjust Amount (where %factor% is a fraction or integer) -> adjust %factor%')
        print('\tMake Vegetarian -> vegify')
        print('\tMake Non-Vegetarian -> meatify')
        print('\tTo Cuisine -> cuisine [latin | asian | indian | british | european | african]')

        print('\n\tTo exit the recipe transformer, use transformation \'stop\'.')
        transformation = input('\nTransformation: ')
        transformation = transformation.lower()
        transformation = transformation.split(' ')

        if transformation[0] == 'stop':
            print('bye!')
            break

        if transformation[0] == 'adjust':
            factor = transformation[1]

            # adjust amounts by factor
            # recipe = new_recipe

            print(f'this much more {factor}')
            continue

        if transformation[0] == 'vegify':
            # make recipe vegetarian
            # recipe = new_recipe

            print('goodbye meat')
            continue

        if transformation[0] == 'meatify':
            # make recipe non-vegetarian
            # recipe = new_recipe

            print('its meat now')
            continue

        if transformation[0] == 'cuisine':
            cuisine = transformation[1]

            # change recipe to the given cuisine
            # recipe = new_recipe

            print(cuisine)
            continue
