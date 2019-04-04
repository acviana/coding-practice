'''
A website requires the users to input username and password to
register. Write a program to check the validity of password input by
users.

Following are the criteria for checking the password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords that match
the criteria are to be printed, each separated by a comma.

Example:

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

ABd1234@1
'''

import string


def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    character_check = {
        'upper_case': False,
        'lower_case': False,
        'digits': False,
        'symbols': False
    }
    for character in password:
        if character in string.ascii_uppercase:
            character_check['upper_case'] = True
        elif character in string.ascii_lowercase:
            character_check['lower_case'] = True
        elif character in string.digits:
            character_check['digits'] = True
        elif character in ['$', '#', '@']:
            character_check['symbols'] = True

    if False in character_check.values():
        return False

    return True


def test_password_checker():
    assert check_password('ABd1234@1') is True
    assert check_password('a F1#') is False
    assert check_password('2w3E*') is False
    assert check_password('2We3345') is False


if __name__ == '__main__':
    test_password_checker()
