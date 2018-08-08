"""
Se le dará un texto, el cual contiene diferentes letras y símbolos de puntuación. Debes encontrar la letra más
frecuente en el texto. La letra retornada debe estar en minúscula. Si se tiene una o más letras con la misma
frecuencia, entonces el resultado será la letra que aparece primero en el alfabeto latino.
"""
from collections import Counter
from operator import itemgetter


def most_wanted_letter(text):
    hist = Counter(text.lower())    # Diccionario con la frecuencia de cada letra
    hist = hist.most_common()       # Lista de tuplas letra-frecuencia
    hist_sorted = sorted(hist, key=itemgetter(0))   # Ordenamos primero por letra
    for letter in sorted(hist_sorted, key=itemgetter(1), reverse=True):     # Ordenamos después por frecuencia
        if letter[0].isalpha():
            return letter[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_wanted_letter("Hello World!") == "l", "Hello test"
    assert most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert most_wanted_letter("One") == "e", "All letter only once."
    assert most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted_letter("abe") == "a", "The First."
    print("Start the long test")
    assert most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

