measures  = {
    'tablespoon measure': ['tablespoon', 'T', 'tbsp']
}

def get_tools(ingredients, directions):

    measurers = ["cup", "tablespoon", "teaspoon", "tablespoons", "teaspoons", "Tablespoon", "Tablespoons", "C", "c", "tsp", "tbsp", "Tbsp", "Tsp"]
    i_cut = ["chopped", "finely chopped", "grated", "mince", "sliced", "halved"]

    d_preparations = ["stir", "stirring", "cook in", "saute in", "cook in a", "saute in a", "sear in", "sear in a", "boil in", "boil in a"]
    possible_tools = ["pan", "pot", "skillet", "saucepan", "sauce pan", "broiler pan", "crockpot", "crock pot", "Crock Pot", "roasting pan"]
    sizes = ["small", "medium", "large", "extra large", "deep", "shallow"]

    # for i in ingredients:
    #     if i[measurement] in measurers:
    #       if i['measure'] == 'tsp':
                # tool_list.append('teaspoon measure')
    for i in ingredients:
        if i.preparation in i_cut:
            tool_list.appen('knife')
            tool_list.appen('cutting board')
        if i.preparation == 'grated':
            tool_list.appen('cheese grater')
        if i.preparation == 'peeled':
            tool_list.appen('peeler')




    tool_list = []
    return tool_list
