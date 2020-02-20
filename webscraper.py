from bs4 import BeautifulSoup
import urllib.request

def is_ingredient(tag):
    return tag.name == "span" and tag.has_attr('itemprop') and tag['itemprop'] == "recipeIngredient"

def is_direction(tag):
    return tag.name == "span" and tag.has_attr('class') and "recipe-directions__list--item" in tag['class']

def parse_recipe(url):
    request_url = urllib.request.urlopen(url)
    web_html = str(request_url.read())
    soup = BeautifulSoup(web_html, 'html.parser')
    ingredients = [span.contents[0] for span in soup.find_all(is_ingredient)]
    soup = BeautifulSoup(web_html, 'html.parser')
    directions = [span.contents[0].strip()[:-2] if len(span.contents) > 0 else '' for span in soup.find_all(is_direction)]
    while '' in directions:
        directions.remove('')
    return {'ingredients': ingredients, 'directions': directions}

if __name__ == '__main__':
    print(parse_recipe("https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=219634%20referringContentType%3Drecipe"))