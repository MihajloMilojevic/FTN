from datetime import datetime

strNone = str(None)


# string
def serialize_string(deserialized_string: str) -> str:
    if deserialized_string is None:
        return strNone
    return deserialized_string


def deserialize_string(serialized_string: str) -> list:
    if serialized_string == strNone:
        return None
    return str(serialized_string)


# int"%x"
def serialize_int(value: int) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_int(serialized_string: str) -> list:
    if serialized_string == strNone:
        return None
    return int(serialized_string)


# float
def serialize_float(value: float) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_float(serialized_string: str) -> list:
    if serialized_string == strNone:
        return None
    return float(serialized_string)


# bool
def serialize_bool(value: bool) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_bool(serialized_string: str) -> list:
    if serialized_string == strNone:
        return None
    return eval(serialized_string)


# Liste
def serialize_list(deserialized_list: list) -> str:
    if deserialized_list is None:
        return strNone
    return str(deserialized_list)


def deserialize_list(serialized_string: str) -> list:
    if serialized_string == strNone:
        return None
    return eval(serialized_string)


# Datum
def serialize_date(deserialized_date: datetime) -> str:
    if deserialized_date is None:
        return strNone
    return datetime.strftime(deserialized_date, "%d.%m.%Y")


def deserialize_date(serialized_string: str) -> datetime:
    if serialized_string == strNone:
        return None
    return datetime.strptime(serialized_string, "%d.%m.%Y")


# Vreme
def serialize_time(deserialized_time: datetime) -> str:
    if deserialized_time is None:
        return strNone
    return datetime.strftime(deserialized_time, "%H:%M:%S")


def deserialize_time(serialized_string: str) -> datetime:
    if serialized_string == strNone:
        return None
    return datetime.strptime(serialized_string, "%H:%M:%S")
