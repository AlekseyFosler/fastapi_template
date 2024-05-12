from enum import Enum, IntEnum, StrEnum


class TemplateStrEnum(StrEnum):
    ONE = 'ONE'
    TWO = 'TWO'
    THREE = 'THREE'


class TemplateIntEnum(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class TemplateEnum(Enum):
    FIRST = 'FIRST'
    SECOND = 'SECOND'
    THIRD = 'THIRD'
