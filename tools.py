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
        'mash': ['potato masher'],
        'poach': ['sauce pot']
    }

    return tools
