from recipe import Recipe


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
        print('\tTo Cuisine -> cuisine [latin | asian | indian | british | european | african]')

        print('\n\tTo exit the recipe transformer, enter \'stop\'.')
        print('\n\tTo start again with a new recipe, simply enter the recipe\'s url.')
        print('\n\tTo show a verbose version of the recipe, enter \'verbose\'. This must be entered every time you '
              'want a verbose output.')

        transformation = input('\nTransformation: ')

        if 'http://' in transformation or 'https://' in transformation:
            recipe = Recipe(transformation)
            break

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
            recipe.vegify()

            print('goodbye meat')
            continue

        if transformation[0] == 'meatify':
            recipe.meatify()

            print('its meat now')
            continue

        if transformation[0] == 'cuisine':
            cuisine = transformation[1]
            recipe.to_cuisine(cuisine)

            print(cuisine)
            continue

        if transformation[0] == 'verbose':
            print(recipe.get_verbose())
            already_printed = True
            continue
