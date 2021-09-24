import sys
import password


def test_equality(actual, expected):
    line_num = sys._getframe(1).f_lineno
    if actual == expected:    
        print(f'Test at line {line_num} OK')
    else:
        print(f'Test at line {line_num} FAILED. Expected {expected} but got {actual}')


def run_tests():
    # Test set_password function
    result_0 = password.set_password('abc')
    test_equality(result_0, ['a','b','c'])

    result_1 = password.set_password('ab c')
    test_equality(result_1, [])
    
    # Test the get_password_string function
    password.set_password('sayhello')
    result_2 = password.get_password_string()
    test_equality(result_2, 'sayhello')

    # Test the add_special_symbol function
    result_3 = password.add_special_symbol('&')
    test_equality(result_3, ['s','a','y','h','e','l','l','o'])

    result_4 = password.add_special_symbol('$')
    test_equality(result_4, ['$','s','a','y','h','e','l','l','o','$'])

    # test the convert_to_numbers function
    result_5 = password.convert_to_numbers()
    test_equality(result_5, ['$','5','a','y','h','e','l','l','0','$'])


run_tests()