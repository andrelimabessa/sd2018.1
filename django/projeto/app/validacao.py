from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):

    if value.isdigit():
        if int(value) < 1 or int(value) > 5:
            raise ValidationError(
                _('%(value)s : Número Inválido.'),
                params={'value': value},
            )
    else:
        raise ValidationError(
                _('%(value)s : Caracter Inválido.'),
                params={'value': value},
            )