# If you don’t want to use exceptions, you can use a function to create your class instead
# (also known as a factory method). You can hide your class from help() by preceding
# the class with an underscore (_), and then create a function in your module that
# checks invariants and instantiates the class. If the invariants are not satisfiable, you
# can return None. Make sure you are using Optional types (as covered in Chapter 4) to
# represent None.


# Note to maintainers, only create this through create_pizza_spec function
from typing import Optional
from dataclasses import dataclass


class _PizzaSpecification:
    """
    This class represents a Pizza Specification for use in
    Automated Pizza Machines.
    The pizza specification is defined by the size of the dough and
    the toppings. Dough should be a whole number between 6 and 12
    inches (inclusive). If anything else is passed in, an AssertionError
    is thrown. The machinery cannot handle less than 6 inches and the
    business case is too costly for more than 12 inches.
    Toppings may have at most one sauce, but you may pass in toppings
    in any order. If there is more than one sauce, an AssertionError is
    thrown. This is done based on our research telling us that
    consumers find two-sauced pizzas do not taste good.
    This class will make sure that sauce is always the first topping,
    regardless of order passed in.
    Toppings are allowed to go above and below cheese
    (the order of non-sauce toppings matters).
    """
    # ... snip class
    pass
 
 
def create_pizza_spec(dough_radius_in_inches: int,
    toppings: list[str]) -> Optional[_PizzaSpecification]:
    try:
        return _PizzaSpecification()
    except:
        return None
    
