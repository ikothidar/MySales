# Other modules
import json
import uuid


class SerializableClass:
    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def is_serializable(obj) -> bool:
        """
        Check if an object is serializable.

        Parameters:
            obj (Any): The object to be checked.

        Returns:
            bool: True if the object is serializable, False otherwise.
        """
        try:
            json.dumps(obj)
            return True
        except:
            return False


def shorten_uuid(input_uuid: uuid.UUID, length: int = 24) -> str:
    """
    Shortens a UUID to a specific length by converting it to
    a hexadecimal string and truncating it.
    Args:
        input_uuid (uuid.UUID): The UUID to be shortened.
        length (int): The desired length of the shortened UUId.
            Defaults to 24.

    Returns:
        str: The shortened UUID as a hexadecimal string.
    """
    # Convert UUID to a hexadecimal string
    str_uuid = str(input_uuid)
    hex_uuid = str_uuid.replace("-", "")

    # Truncate to the desired length
    truncated_hex = hex_uuid[:length]

    return truncated_hex


def generate_uuid(length: int = None) -> str:
    """
    Generate a universally unique identifier (UUID) as a string.

    Args:
        length (int, optional): The length of the shortened UUID.
            Defaults to None.

    Returns:
        str: The generated UUID as a string.

    Example:
        >> generate_uuid()
        'dfc6f4a9-2a97-4c1c-9a04-9b09c6e4b7be'
        >> generate_uuid(8)
        'dfc6f4a9'
    """
    if length:
        return shorten_uuid(uuid.uuid4())

    str_uuid = str(uuid.uuid4())
    return str_uuid


def get_name_by_gst(gst_number: str):
    """
    Get name of the party based on gst number passed.

    Args:
        gst_number (str): The gst number to query for.

    Returns:
        The name associated with the gst_number, or none if not found.
    """
    from mysales.models.models import GSTDetails

    gst_data = GSTDetails.query.filter_by(gst_number=gst_number).first()

    if gst_data:
        return gst_data.name
    else:
        return None
