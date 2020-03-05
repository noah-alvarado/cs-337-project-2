# Recipes Tool
## Initialization
Ensure that you are running Python 3.7 or higher using the command `python3 --version`. The output should be of the form:
```commandline
Noahs-MacBook-Air:cs-337-project-2 noahalvarado$ python3 --version
Python 3.7.4
```

Install `virtualenv` and initialize a virtual environment.
```commandline
python3 -m pip install virtualenv
python3 -m venv venv
```

Swtich to the virtual environment you just created and install the necessary packages.
```commandline
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
Now, you are ready to run Recipes Tool.

## Running
To use our tool, run the command:
```commandline
python3 recipes_tool.py
```

Enter the url of the recipe at the prompt that appears.
```commandline
Recipe URL: https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=86587%20referringContentType%3Drecipe
```

Now you can select a list

## Usage
The first thing you see when running our tool is a prompt to enter a recipe url.
Simply paste the recipe in this area and hit return.

This will automatically load the online recipe, parse the ingredients and step, and display a prompt for transforming the recipe.

The [available transformations](#transformations) are:
- [Adjust amount](#adjust-amount)
- [Make vegetarian](#make-vegetarian)
- [Make non-vegetarian](#make-non-vegetarian)
- [Change cuisine](#change-cuisine)
- [Make healthier](#make-more-healthy)
- [Make less healthy](#make-less-healthy)

Also available at this prompt are quitting the program, verbosely printing the recipe, and resetting to a new recipe.
These are referred to as [reserved transformations](#reserved-transformations).

## Transformations
### Adjust Amount
few

### Make Vegetarian
few

### Make Non-vegetarian
few

### Change Cuisine
few

### Make More Healthy
few

### Make Less Healthy
few

### Reserved Transformations