from typing import TypedDict

class PersonDict(TypedDict):
    name: str
    age: int
    occupation: str

# Usage
person: PersonDict = {"name": "Alice", "age": 30, "occupation": "Engineer"}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}

# Accessing values
print(person["name"])  # Output: Alice

# Adding additional fields (This will not raise an error, but might fail static type checks)
person["hobby"] = "Painting"