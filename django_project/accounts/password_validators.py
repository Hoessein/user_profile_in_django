from django.core.exceptions import ValidationError
import re


class HasLowerCaseValidator:
    def __init__(self):
        self.message = "The password must contain at least one lowercase character."

    def validate(self, password, user=None):
        if re.search('[a-z]', password) is None:
            raise ValidationError(self.message, code='missing_lower_case')

    def get_help_text(self):
        return self.message


class HasUpperCaseValidator:
    def __init__(self):
        self.message = "The password must contain at least one uppercase character."

    def validate(self, password, user=None):
        if re.search('[A-Z]', password) is None:
            raise ValidationError(self.message, code='missing_upper_case')

    def get_help_text(self):
        return self.message


class HasNumberValidator:
    def __init__(self):
        self.message = "The password must contain at least one numeric character."

    def validate(self, password, user=None):
        if re.search('[0-9]', password) is None:
            raise ValidationError(self.message, code='missing_numeric')

    def get_help_text(self):
        return self.message


class HasSymbolValidator:
    def __init__(self):
        self.message = "The password must contain at least one non-alphanumeric character (symbol)."

    def validate(self, password, user=None):
        if re.search('[^A-Za-z0-9]', password) is None:
            raise ValidationError(self.message, code='missing_symbol')

    def get_help_text(self):
        return self.message