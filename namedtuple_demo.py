from collections import namedtuple

NuritionInformation = namedtuple('NuritionInformation', ['calories', 'fat', 'carbohydrates'])
nutrition = NuritionInformation(calories=100, fat=5, carbohydrates=10)
print(nutrition.calories)