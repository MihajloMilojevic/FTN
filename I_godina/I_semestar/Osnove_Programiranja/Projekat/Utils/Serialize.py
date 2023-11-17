from datetime import datetime

strNone = str(None)


# string
def serialize_string(string: str) -> str:
    if string is None:
        return strNone
    return string


def deserialize_string(string: str) -> list:
    if string == strNone:
        return None
    return str(string)


# int
def serialize_int(value: int) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_int(str: str) -> list:
    if str == strNone:
        return None
    return int(str)


# float
def serialize_float(value: float) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_float(str: str) -> list:
    if str == strNone:
        return None
    return float(str)


# bool
def serialize_bool(value: bool) -> str:
    if value is None:
        return strNone
    return str(value)


def deserialize_bool(str: str) -> list:
    if str == strNone:
        return None
    return eval(str)


# Liste
def serialize_list(list: list) -> str:
    if list is None:
        return strNone
    return str(list)


def deserialize_list(str: str) -> list:
    if str == strNone:
        return None
    return eval(str)


# Datum
def serialize_date(date: datetime) -> str:
    if date is None:
        return strNone
    return datetime.strftime(date, "%d.%m.%Y")


def deserialize_date(str: str) -> datetime:
    if str == strNone:
        return None
    return datetime.strptime(str, "%d.%m.%Y")


# Vreme
def serialize_time(time: datetime) -> str:
    if time is None:
        return strNone
    return datetime.strftime(time, "%H:%M:%S")


def deserialize_time(str: str) -> datetime:
    if str == strNone:
        return None
    return datetime.strptime(str, "%H:%M:%S")
