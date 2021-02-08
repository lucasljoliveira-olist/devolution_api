

def validate_type(value, type, key):
    if not isinstance(value, type):
        raise TypeError(f'{key.capitalize()} must be {type}.')


def validate_string_not_empty(value, key):
    if not value.strip():
        raise ValueError(f'{key.capitalize()} cannot be empty')


def validate_length(value, max_len, key):
    if len(value) > 100:
        raise ValueError(
            f'{key.capitalize()} connot be bigger than {max_len} characters.')
