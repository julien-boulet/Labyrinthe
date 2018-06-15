from enum import Enum


class BaseEnum(Enum):

    def get_value(self):
        return self._value_
