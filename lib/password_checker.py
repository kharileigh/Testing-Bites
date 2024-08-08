# File: lib/password_checker.py

class PasswordChecker:
    # - checking length of given password is greater or equal to 8 characters
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
