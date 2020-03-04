from recipe import Recipe


if __name__ == '__main__':
    url = input('Recipe URL: ')
    recipe = Recipe(url)

    # loop forever so we can keep performing transformations
    while True:
        # print the recipe
        print(recipe)

        # print available transformations
        print('\nAvailable transformations:')

        print('\tAdjust Amount (where %factor% is a fraction or integer) -> adjust %factor%')
        print('\tMake Vegetarian -> vegify')
        print('\tMake Non-Vegetarian -> meatify')
        print('\tTo Cuisine -> cuisine [mexican | italian]')

        print('\n\tTo exit the recipe transformer, use transformation \'stop\'.')
        transformation = input('\nTransformation: ')
        transformation = transformation.lower()
        transformation = transformation.split(' ')

        if transformation[0] == 'stop':
            print('Goodbye!')
            break

        if transformation[0] == 'adjust':
            factor = transformation[1]
            recipe.adjust_portions(factor)
            continue

        if transformation[0] == 'vegify':
            recipe.vegify()
            continue

        if transformation[0] == 'meatify':
            recipe.meatify()
            continue

        if transformation[0] == 'cuisine':
            cuisine = transformation[1]

            allowed_cuisines = ['mexican', 'italian']
            if cuisine not in allowed_cuisines:
                print('Error! Cuisine must be in [\'mexican\', \'italian\']')
                continue

            recipe.to_cuisine(cuisine)
            continue
