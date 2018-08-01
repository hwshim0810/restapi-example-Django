from django.utils import six
from django.contrib.auth.validators import (
    ASCIIUsernameValidator,
    UnicodeUsernameValidator,
)


def username_validator():
    return UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
