"""
Se te dará una lista no vacía de enteros (X). Para esta misión, deberás retornar una lista que consista únicamente
de elementos no únicos. Para hacerlo, necesitarás eliminar todos los elementos que sean únicos (elementos que
aparezcan una sola vez en la lista dada). Al resolver esta misión, no cambies el orden de la lista.
"""

from collections import Counter


def non_unique_elements(data: list) -> list:
    hist = Counter(data)
    return [element for element in data if hist[element] > 1]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
