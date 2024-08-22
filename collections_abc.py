import collections

class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients
        
    def __contains__(self, value: str):
        return value in self.ingredients
    
    def __iter__(self):
        return iter(self.ingredients)
    
    def __len__(self):
        return len(self.ingredients)