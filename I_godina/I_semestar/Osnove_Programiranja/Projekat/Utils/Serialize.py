from datetime import datetime

# Liste
def serialize_list(list: list) -> str:
    return str(list)

def deserialize_list(str: str) -> list:
    return eval(str)

# Datum
def serialize_date(date: datetime) -> str:
    return datetime.strftime(date, "%x")

def deserialize_date(str: str) -> datetime:
    return datetime.strptime(str, "%x")

# Vreme
def serialize_time(time: datetime) -> str:
    return datetime.strftime(time, "%X")

def deserialize_time(str: str) -> datetime:
    return datetime.strptime(str, "%X")


