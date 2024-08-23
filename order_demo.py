from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable, Optional
from copy import deepcopy


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
class Ingredient:
    name: str
    brand: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP
    
    def __add__(self, rhs: 'Ingredient'): # INFO: To fix this, you can use a forward reference by placing Ingredient in quotes. 
                                          # INFO: This tells Python to treat Ingredient as a string and to resolve it later once the class definition is complete.
        
        # make sure we are adding the same ingredient
        assert ( self.name, self.brand) == ( rhs.name, rhs.brand)
        # build up conversion chart (lhs, rhs): multiplication factor
        conversion: dict[tuple[ImperialMeasure, ImperialMeasure], float] = {
        (ImperialMeasure.CUP, ImperialMeasure.CUP): 1,
        (ImperialMeasure.CUP, ImperialMeasure.TABLESPOON): 16,
        (ImperialMeasure.CUP, ImperialMeasure.TEASPOON): 48,
        (ImperialMeasure.TABLESPOON, ImperialMeasure.CUP): 1/ 16,
        (ImperialMeasure.TABLESPOON, ImperialMeasure.TABLESPOON): 1,
        (ImperialMeasure.TABLESPOON, ImperialMeasure.TEASPOON): 3,
        (ImperialMeasure.TEASPOON, ImperialMeasure.CUP): 1/ 48,
        (ImperialMeasure.TEASPOON, ImperialMeasure.TABLESPOON): 1/3,
        (ImperialMeasure.TEASPOON, ImperialMeasure.TEASPOON): 1
        }
        return Ingredient(rhs.name, rhs.brand, rhs.amount + self.amount * conversion[(rhs.units, self.units)], rhs.units)


class Order:
    ''' An Order class that represents a list of ingredients '''
    def __init__(self, recipes: Iterable[Recipe]):
        self.__confirmed = False
        self.__ingredients: set[Ingredient] = set()
        for recipe in recipes:
            for ingredient in recipe.ingredients:
                self.add_ingredient(ingredient)
                
    def get_ingredients(self) -> list[Ingredient]:
        ''' Return a alphabetically sorted list of ingredients '''
        # return a copy so that users won't inadvertently mess with
        # our internal data
        return sorted(deepcopy(self.__ingredients), key=lambda ing: ing.name)
    
    def _get_matching_ingredients(self, ingredients: Ingredient) -> Optional[Ingredient]:
        try:
            return next(ing for ing in self.__ingredients if ((ing.name, ing.brand) == (ingredients.name, ingredients.brand)))
        except StopIteration:
            return None
        
    def add_ingredient(self, ingredient: Ingredient):
        ''' adds the ingredient if it's not already added,
            or increases the amount if it has        
        '''
        self.__disallow_modification_if_confirmed()
        target_ingredient = self._get_matching_ingredients(ingredient)
        if target_ingredient is None:
            # ingredient for the first time - add it
            self.__ingredients.add(ingredient)
        else:
            # add ingredient to existing set
            target_ingredient += ingredient
            
    def __disallow_modification_if_confirmed(self):
        if self.__confirmed:
            raise OrderAlreadyFinalizedError('Order is confirmed - changing it is not allowed')
        
    def confirm(self):
        self.__confirmed = True
        
    def unconfirmed(self):
        self.__confirmed = False
        
    def is_confirmed(self):
        return self.__confirmed


@dataclass       
class _GroceryList:
    order: Order
    inventory: Inventory
    
    def unreserved_items():
        pass
    
    def has_reserved_items():
        pass
    
    
@contextmanager
def create_grocery_list(order: Order, inventory: Inventory):
    grocery_list = _GroceryList(order, inventory)
    try:
        yield grocery_list
    finally:
        if grocery_list.has_reserved_items():
            grocery_list.unreserved_items()

class OrderAlreadyFinalizedError(RuntimeError):
    # inheriting from RuntimeError to allow users to provide a message
    # when raising this exception
    pass
