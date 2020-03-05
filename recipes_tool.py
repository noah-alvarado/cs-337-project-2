from recipe import Recipe


def print_replacements(changes):
    if len(changes) == 0:
        print('No changes were made!')
        return

    swaps = list(filter(lambda pair: pair[0] is not None, changes))
    additions = list(filter(lambda pair: pair[0] is None, changes))

    if len(swaps) > 0:
        for old, new in zip(*swaps):
            print('Replaced {} with {}'.format(old, new))
        print()

    if len(additions) > 0:
        for _, new in zip(*additions):
            print('Added {}'.format(new))
        print()


if __name__ == '__main__':
    url = input('Recipe URL: ')
    recipe = Recipe(url)

    # loop forever so we can keep performing transformations
    already_printed = False
    while True:
        # print the recipe
        if not already_printed:
            print(recipe)

        already_printed = False

        # print available transformations
        print('\nAvailable transformations:')

        print('\tAdjust Amount (where %factor% is a fraction or integer) -> adjust %factor%')
        print('\tMake Vegetarian -> vegify')
        print('\tMake Non-Vegetarian -> meatify')
        print('\tTo Cuisine -> cuisine [italian | mexican]')
        print('\tMake Healthier -> healthy')
        print('\tMake Less Healthy -> not-healthy')

        print('\n\tTo exit the recipe transformer, enter \'stop\'.')
        print('\n\tTo start again with a new recipe, simply enter the recipe\'s url.')
        print('\n\tTo show a verbose version of the recipe, enter \'verbose\'. This must be entered every time you '
              'want a verbose output.')

        transformation = input('\nTransformation: ')

        if 'http://' in transformation or 'https://' in transformation:
            recipe = Recipe(transformation)
            continue

        transformation = transformation.lower()
        transformation = transformation.split(' ')

        if transformation[0] == 'stop':
            print('bye!')
            break

        if transformation[0] == 'adjust':
            factor = transformation[1]
            try:
                factor = float(factor)
            except:
                print('Invalid Input :(')
                continue

            print('Adjusting the recipe by a factor of: ', factor)
            recipe.adjust_portions(factor)
            continue

        if transformation[0] == 'vegify':
            replacements = recipe.vegify()
            replacements = list(replacements)

            # print what was changed
            print_replacements(replacements)

            # change steps to reflect changed ingredients
            recipe.change_step_ingredients(replacements)

            continue

        if transformation[0] == 'meatify':
            replacements = recipe.meatify()
            replacements = list(replacements)

            # print what was changed
            print_replacements(replacements)

            # change steps to reflect changed ingredients
            recipe.change_step_ingredients(replacements)

            continue

        if transformation[0] == 'cuisine':
            cuisine = transformation[1]

            if cuisine in ['mexican', 'italian']:
                replacements = recipe.to_cuisine(cuisine)
                replacements = list(replacements)

                # print what was changed
                print_replacements(replacements)

                # change steps to reflect changed ingredients
                recipe.change_step_ingredients(replacements)

                continue

        if transformation[0] == 'healthy':
            replacements = recipe.healthier()
            replacements = list(replacements)

            # print what was changed
            print_replacements(replacements)

            # change steps to reflect changed ingredients
            recipe.change_step_ingredients(replacements)

            continue

        if transformation[0] == 'not-healthy':
            replacements = recipe.less_healthy()
            replacements = list(replacements)

            # print what was changed
            print_replacements(replacements)

            # change steps to reflect changed ingredients
            recipe.change_step_ingredients(replacements)

            continue

        if transformation[0] == 'verbose':
            print(recipe.get_verbose())
            already_printed = True
            continue

        print('\nSorry, that tranformation was not recognized. Please check your spelling and try again.\n')
        already_printed = True
