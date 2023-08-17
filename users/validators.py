import re
from rest_framework.serializers import ValidationError

PHONE_NUMBER_REGEX = re.compile(r'^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$')

def validate_phone_number(value):
    if not PHONE_NUMBER_REGEX.match(value):
        raise ValidationError(u'Invalid phone number')
