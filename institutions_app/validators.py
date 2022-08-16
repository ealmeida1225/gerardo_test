from django.core.exceptions import ValidationError
import re

def validate_nif(value):
    pattern = "\d{8}[A-Z]"
    if not re.fullmatch(pattern, value):
        raise ValidationError(
            f'{value} does not match the required NIF format'
        )