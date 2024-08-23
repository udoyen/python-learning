import datetime
from dataclasses import dataclass
from enum import Enum, auto


class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()
    
class Broth(Enum):
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()
    

@dataclass(frozen=True)
# Ingredients added into the borth
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP
    
    
@dataclass
class Recipe:
    aromatics: set[Ingredient]
    broth: Broth
    vegetables: set[Ingredient]
    meats: set[Ingredient]
    starches: set[Ingredient]
    garnishes: set[Ingredient]
    time_to_cook: datetime.timedelta
    
    def make_vegetarian(self):
        # The clear() function is not an inbuilt function specific to data classes in Python. Instead, 
        # it is a method of Python's mutable collection types, such as list, 
        # set, and dict. The clear() method removes all items from the collection, effectively emptying it.
        self.meats.clear() 
        self.broth = Broth.VEGETABLE
        
    def get_ingredient_names(self):
        ingredients = (self.aromatics | self.vegetables | self.meats | self.starches | self.garnishes)
        return ({i.name for i in ingredients} | {self.broth.name.capitalize() + " broth"})
    
    
# Implementation of data classes

pepper = Ingredient("Pepper", 1, ImperialMeasure.TABLESPOON)
garlic = Ingredient("Garlic", 2, ImperialMeasure.TEASPOON)
carrots = Ingredient("Carrots", .25, ImperialMeasure.CUP)
celery = Ingredient("Celery", .25, ImperialMeasure.CUP)
onions = Ingredient("Onions", .25, ImperialMeasure.CUP)
parsley = Ingredient("Parsley", 2, ImperialMeasure.TABLESPOON)
noodles = Ingredient("Noodles", 1.5, ImperialMeasure.CUP)
chicken = Ingredient("Chicken", 1.5, ImperialMeasure.CUP)


chicken_noodle_soup = Recipe(
    aromatics={pepper, garlic},
    broth=Broth.CHICKEN,
    vegetables={celery, onions, carrots},
    meats={chicken},
    starches={noodles},
    garnishes={parsley},
    time_to_cook=datetime.timedelta(minutes=60)
    
)


# Implementation

from copy import deepcopy
# make a deep copy so that changing one soup
# does not change the original
noodle_soup = deepcopy(chicken_noodle_soup)
noodle_soup.make_vegetarian()
print(noodle_soup.get_ingredient_names())
# >>> { 'Garlic', 'Pepper', 'Carrots', 'Celery', 'Onions',
#  'Noodles', 'Parsley', 'Vegetable Broth'}
