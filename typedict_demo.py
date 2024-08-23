from typing import TypedDict

class Range(TypedDict):
    min: float
    max: float
    
range_example = Range(min=50.0, max=200.0)
    
class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float
    
nutrition_info_example = NutritionInformation(
    value=150,
    unit='kcal',
    confidenceRange95Percent=Range(min=140.0, max=160.0),
    standardDeviation=5.0
)
    
nutritioninformation: NutritionInformation = {
    "value": 1,
    "unit": 'grams',
    "confidenceRange95Percent": {"min": 1, "max": 10},
    "standardDeviation": 34
}
    

class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


recipe_nutrition_info_example = RecipeNutritionInformation(
    recipes_used=5,
    calories=NutritionInformation(
        value=500,
        unit='kcal',
        confidenceRange95Percent=Range(min=450.0, max=550.0),
        standardDeviation=20.0
    ),
    fat=NutritionInformation(
        value=30,
        unit='g',
        confidenceRange95Percent=Range(min=28.0, max=32.0),
        standardDeviation=1.5
    ),
    protein=NutritionInformation(
        value=40,
        unit='g',
        confidenceRange95Percent=Range(min=38.0, max=42.0),
        standardDeviation=2.0
    ),
    carbs=NutritionInformation(
        value=100,
        unit='g',
        confidenceRange95Percent=Range(min=95.0, max=105.0),
        standardDeviation=3.0
    )
)

