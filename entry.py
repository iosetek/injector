class Entry:
    def __init__(self, key, value, encoding, allowAddingSpaces):
        self.key = key
        self.value = value
        self.encoding = encoding
        if not allowAddingSpaces in ["allow", "disallow"]:
            raise InvalidValueException
        self.allowAddingSpaces = allowAddingSpaces == "allow"


    def first_key_byte(self):
        return self.key[0]

class InvalidValueException(Exception):
    pass