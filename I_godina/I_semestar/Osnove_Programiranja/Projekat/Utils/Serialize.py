from datetime import datetime

strNone = str(None)

# string
def serialize_string(str: str) -> str:
    if str is None:
        return strNone
    return str
def deserialize_string(str: str) -> list:
    if str == strNone:
        return None
    return eval(str)

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
    return bool(str)

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
        return str(None)
    return datetime.strftime(date, "%x")

def deserialize_date(str: str) -> datetime:
    if str == str(None):
        return None
    return datetime.strptime(str, "%x")

# Vreme
def serialize_time(time: datetime) -> str:
    return datetime.strftime(time, "%X")

def deserialize_time(str: str) -> datetime:
    return datetime.strptime(str, "%X")


