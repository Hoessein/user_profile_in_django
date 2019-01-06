from django.core.exceptions import ValidationError


import re

# https://docs.djangoproject.com/en/2.1/topics/auth/passwords/#writing-your-own-validator


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


class UserProfileAttributeSimilarityValidator:

    def __init__(self):
        self.message = "Your password can't be too similar to your other personal information."

    def validate(self, password, user=None):
        if not user:
            return

        not_allowed_attributes = []

        if user:
            not_allowed_attributes.append(user.username.lower())
            if hasattr(user, 'profile'):
                not_allowed_attributes.append(user.profile.first_name.lower())
                not_allowed_attributes.append(user.profile.last_name.lower())

            for attribute in not_allowed_attributes:
                if attribute:
                    # additional check to prevent default model fields to be
                    # added to not_allowed_attributes
                    if attribute in password.lower():
                        raise ValidationError(self.message)

    def get_help_text(self):
        return self.message
