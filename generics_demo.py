from typing import TypeVar

T = TypeVar('T')
def reverse(coll: list[T]) -> list[T]:
    return coll[::-1]

