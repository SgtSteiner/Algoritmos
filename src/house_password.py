"""
La contraseña será considerada suficientemente fuerte si el largo es mayor o igual a 10 caracteres, tiene por lo
menos un dígito, así como una letra en mayúscula y una letra en minúscula. La contraseña contiene solo letras latinas
o dígitos ASCII.
"""


def check_password(data: str) -> bool:
    digit_ok = False
    upper_ok = False
    lower_ok = False

    if len(data) < 10:
        return False
    else:
        for letter in data:
            if letter.isupper():
                upper_ok = True
            if letter.islower():
                lower_ok = True
            if letter.isdigit():
                digit_ok = True

    return digit_ok and upper_ok and lower_ok


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_password('A1213pokl') == False, "1st example"
    assert check_password('bAse730onE4') == True, "2nd example"
    assert check_password('asasasasasasasaas') == False, "3rd example"
    assert check_password('QWERTYqwerty') == False, "4th example"
    assert check_password('123456123456') == False, "5th example"
    assert check_password('QwErTy911poqqqq') == True, "6th example"
    print("Completo OK!")
