from dataclasses import dataclass
from typing import Literal

@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool
    
@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: set[Literal["Mustard", "Ketchup"]]