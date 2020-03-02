from common_data import descriptors, measures, preparations, special_descriptors

def get_tools(ingredients, directions):

    tools = []

    for i in ingredients:
        if i['measure'] in measures:
            tools.append(measures['measure'])

    prep = {
        'basted': ['baster'],
        'blended': ['blender'],
        'julienned': ['cutting board', 'knife'],
        'mashed': ['potato masher'],
        'minced': ['cutting board', 'knife'],
        'chopped': ['cutting board', 'knife'],
        'grated': ['cheese grater'],
        'diced': ['cutting board', 'knife'],
        'peeled': ['peeler'],
        'sliced': ['cutting board', 'knife'],
        'slivered': ['cutting board', 'knife'],
        'halved': ['cutting board', 'knife'],
        'stirred': ['spoon'],
        'mixed': ['spoon'],
        'whisked': ['whisk'],
        'pulverized': ['food processor'],
        'pureed': ['food processor'],
        'tenderized': ['meat pounder']
    }
    tasks = {
        'saute': ['pan'],
        'boil': ['pot'],
        'simmer': ['pot'],
        'grill': ['grill'],
        'char': ['grill'],
        'carmelize': ['pan'],
        'browned': ['oven'],
        'whip': ['whisk'],
        'combine': ['spoon', 'mixing bowl'],
        'puree': ['food processor'],
        'stir to combine': ['spoon', 'mixing bowl'],
        'blanche': ['pot', 'strainer', 'ice bath'],
        'braise': ['saucepan', 'oven'],
        'fried': ['pot', 'strainer'],
        'hard-boiled': ['pot'],
        'soft-boiled': ['pot'],
        'stew': ['large saucepot'],
        'sear': ['pan'],
        'scramble': ['whisk'],
        'reduced': ['sauce pot'],
        'pulverize': ['mortar and pestle'],
        'grind': ['mortar and pestle'],
        'pan-fry': ['pan'],
        'melt': ['bowl'],
        'mash': ['potato masher']
    }

    # measurers = ["cup", "tablespoon", "teaspoon", "tablespoons", "teaspoons", "Tablespoon", "Tablespoons", "C", "c", "tsp", "tbsp", "Tbsp", "Tsp"]
    # i_cut = ["chopped", "finely chopped", "grated", "mince", "sliced", "halved"]
    #
    # d_preparations = ["stir", "stirring", "cook in", "saute in", "cook in a", "saute in a", "sear in", "sear in a", "boil in", "boil in a"]
    # possible_tools = ["pan", "pot", "skillet", "saucepan", "sauce pan", "broiler pan", "crockpot", "crock pot", "Crock Pot", "roasting pan"]
    # sizes = ["small", "medium", "large", "extra large", "deep", "shallow"]
    #
    # # for i in ingredients:
    # #     if i[measurement] in measurers:
    # #       if i['measure'] == 'tsp':
    #             # tool_list.append('teaspoon measure')
    # for i in ingredients:
    #     if i.preparation in i_cut:
    #         tool_list.appen('knife')
    #         tool_list.appen('cutting board')
    #     if i.preparation == 'grated':
    #         tool_list.appen('cheese grater')
    #     if i.preparation == 'peeled':
    #         tool_list.appen('peeler')
    #
    #
    #
    #
    # tool_list = []
    return tools
