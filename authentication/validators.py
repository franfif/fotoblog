from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'The password must contain a letter', code='password_no_letters')

    def get_help_text(self):
        return 'Your password must contain at least one upper or lower case letter.'


class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not any(char.is_digit() for char in password):
            raise ValidationError(
                'The password must contain a digit', code='password_no_digits')

    def get_help_text(self):
        return 'Your password must contain at least one digit.'
