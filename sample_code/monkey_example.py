import time

class Ingredient:
    def __init__(self, ingredients, count, utensil):
        self.ingredients = ingredients
        self.count = count
        self.utensil = utensil


# Pasta with Sausage Automated Maker 
italian_sausage = Ingredient('Italian Sausage', 4, 'links')
olive_oil = Ingredient('Olive Oil', 1, 'tablespoon')
plum_tomato = Ingredient('Plum Tomato', 6, '')
garlic = Ingredient('Garlic', 4, 'cloves')
black_pepper = Ingredient('Black Pepper', 2, 'teaspoons')
basil = Ingredient('Basil Leaves', 1, 'cup')
pasta = Ingredient('Rigatoni', 1, 'pound')
salt = Ingredient('Salt', 1, 'tablespoon')
water = Ingredient('Water', 6, 'quarts')
cheese = Ingredient('Pecorino Romano', 2, "ounces")


class Recipe:
    def __init__(self, recipe_number, ingredients: list[Ingredient]): 
        self.recipe_number = recipe_number
        self.ingredients = ingredients
        
    def clear_ingredients(self):
        pass
    
    def get_ingredients(self, name: str):
        pass

pasta_with_sausage = Recipe(6, [ italian_sausage, olive_oil, plum_tomato, garlic, black_pepper, pasta, salt, water, cheese, basil])


class Receptacle:
    def __init__(self, name):
        self.name = name
        
    def add(self, ingredient: Ingredient):
        pass

class adjust_recipe:
    pass


class recipe_maker:
    pass


def make_pasta_with_sausage(servings):
    sauté_pan = Receptacle('Sauté Pan')
    pasta_pot = Receptacle('Stock Pot')
    adjusted_recipe = adjust_recipe(pasta_with_sausage, servings)
    
    print("Prepping ingredients")
    
    adjusted_tomatoes = adjusted_recipe.get_ingredient('Plum Tomato')
    adjusted_garlic = adjusted_recipe.get_ingredient('Garlic')
    adjusted_cheese = adjusted_recipe.get_ingredient('Pecorino Romano')
    adjusted_basil = adjusted_recipe.get_ingredient('Basil Leaves')
    garlic_and_tomatoes = recipe_maker.dice(adjusted_tomatoes, adjusted_garlic)
    
    grated_cheese = recipe_maker.grate(adjusted_cheese)
    
    sliced_basil = recipe_maker.chiffonade(adjusted_basil)
    
    print("Cooking Pasta") 
    pasta_pot.add(adjusted_recipe.get_ingredient('Water'))
    pasta_pot.add(adjusted_recipe.get_ingredient('Salt'))
    recipe_maker.put_receptacle_on_stovetop(pasta_pot, heat_level=10)
    
    pasta_pot.add(adjusted_recipe.get_ingredient('Rigatoni'))
    recipe_maker.set_stir_mode(pasta_pot, ( 'every minute'))
    
    print("Cooking Sausage")
    sauté_pan.add(adjusted_recipe.get_ingredient('Olive Oil'))
    heat_level = recipe_maker.HeatLevel.MEDIUM
    recipe_maker.put_receptacle_on_stovetop(sauté_pan, heat_level)
    sauté_pan.add(adjusted_recipe.get_ingredient('Italian Sausage'))
    recipe_maker.brown_on_all_sides('Italian Sausage')
    cooked_sausage = sauté_pan.remove_ingredients(to_ignore=[ 'Olive Oil'])
    
    sliced_sausage = recipe_maker.slice(cooked_sausage, thickness_in_inches=.25)
    
    print("Making Sauce")
    sauté_pan.add(garlic_and_tomatoes)
    recipe_maker.set_stir_mode(sauté_pan, ( 'every minute'))
    while recipe_maker.is_not_cooked('Rigatoni'):
        time.sleep(30)
    cooked_pasta = pasta_pot.remove_ingredients(to_ignore=[ 'Water', 'Salt'])
    
    sauté_pan.add(sliced_sausage)
    while recipe_maker.is_not_cooked('Italian Sausage'):
        time.sleep(30)





