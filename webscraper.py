from bs4 import BeautifulSoup

import requests


def is_ingredient(tag):
    return tag.name == "span" and tag.has_attr('itemprop') and tag['itemprop'] == "recipeIngredient"


def is_direction(tag):
    return tag.name == "span" and tag.has_attr('class') and "recipe-directions__list--item" in tag['class']


def parse_recipe(url):
    response = requests.get(url)

    web_html = response.text
    soup = BeautifulSoup(web_html, 'html.parser')

    ingredients = [span.contents[0] for span in soup.find_all(is_ingredient)]

    soup = BeautifulSoup(web_html, 'html.parser')

    directions = [span.contents[0].strip()[:-2] if len(span.contents) > 0 else '' for span in soup.find_all(is_direction)]

    while '' in directions:
        directions.remove('')

    return {'ingredients': ingredients, 'directions': directions}