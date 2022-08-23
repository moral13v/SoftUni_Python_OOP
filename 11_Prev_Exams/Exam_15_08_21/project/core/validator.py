class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_or_equal_to_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number: int, min_val: int, max_val: int, message: str):
        if number < min_val or number > max_val:
            raise ValueError(message)
