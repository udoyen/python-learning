from dataclasses import dataclass, field

@dataclass(eq=True, order=True)
class NutritionInformation:
    calories: float
    fat: float = field(default=0, metadata={"unit": "grams"})
    carbohydrates: float = field(default=0, metadata={"unit": "grams"})
    
nutritionals = [ NutritionInformation(calories=100, fat=1, carbohydrates=3 ),
 NutritionInformation(calories=50, fat=6, carbohydrates=4 ),
 NutritionInformation(calories=125, fat=12, carbohydrates=3 )]


print(sorted(nutritionals))
    