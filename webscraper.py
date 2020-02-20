from bs4 import BeautifulSoup
import urllib.request

def is_ingredient(tag):
    return tag.name == "span" and tag.has_attr('itemprop') and tag['itemprop'] == "recipeIngredient"

def is_direction(tag):
    return tag.name == "span" and tag.has_attr('class') and tag['class'] == "recipe-directions__list--item"

def parse_recipe(url):
    request_url = urllib.request.urlopen(url)
    web_html = str(request_url.read())
    soup = BeautifulSoup(web_html, 'html.parser')
    ingredients = [span.contents[0] for span in soup.find_all(is_ingredient)]
    directions = [span.contents[0] for span in soup.find_all(is_direction)]
    return {'ingredients': ingredients, 'directions': directions}

if __name__ == '__main__':
    print(parse_recipe("https://www.allrecipes.com/recipe/219634/chef-johns-french-fries/"))