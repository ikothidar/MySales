def format_date(date_obj, format: str = '%Y-%m-%d') -> str:
    """
    Convert datetime object to string date.

    Args:
        date_obj: datetime object to convert,
        format: format for date to convert,

    Returns:
        datetime convert to specified string format.
    """
    return date_obj.strftime(format)


def convert_list_to_strings(input_list: list) -> list:
    """
    Convert given list to list of string
    Args:
        input_list: list to convert to.

    Returns:
        list of string after conversion.
    """
    return list(map(str, input_list))
