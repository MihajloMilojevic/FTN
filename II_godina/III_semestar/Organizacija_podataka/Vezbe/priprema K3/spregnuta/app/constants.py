from enum import IntEnum

ATTRIBUTES = ["id", "name", "q", "status"]
FMT = "i10sdi"
CODING = "ascii"

B = 5
F = 5


class RecordStatus:
    FREE = 0
    ACTIVE = 1
    DELETED = 2
