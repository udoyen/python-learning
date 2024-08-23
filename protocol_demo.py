from typing import Protocol, runtime_checkable

@runtime_checkable
class Splittable(Protocol):
    cost: int
    name: str
    
    def split_in_half(self) -> tuple['Splittable', 'Splittable']:
        """ No implementation needed"""
        pass
    
    
class BLTSandwich:
    def __init__(self):
        self.cost = 6.95
        self.name = 'BLT'
        
    def split_in_half(self) -> tuple['BLTSandwich', 'BLTSandwich']: #TODO: Fix this bug, let's know why this ('BLTsandwich', 'BLTsandwich) isn't working
        # Instructions for how to split a sandwich in half
        # Cut along diagonal, wrap separately, etc.
        # Return two sandwiches in returN
        pass
    

# The typechecker will detect that a BLTSandwich is Splittable just by virtue of the
# fields and method it has defined. This simplifies class hierarchies immensely. You
# don’t need a complicated tree structure, even as you add more protocols. You can
# simply define a different protocol for each set of required behaviors, including Sharea
# ble, Substitutable, or PickUppable. Functions that depend on those behaviors can
# then rely on those protocols instead of any sort of base class. The original classes
# don’t need to change in any form, as long as they implement the needed functionality.
def split_dish(order: Splittable) -> tuple[Splittable, Splittable]:
    pass