from enum import Enum
class EnumType(Enum):
    @classmethod
    def values(cls):
        values = [member.value for member in cls] 
        return values
    
    def names(cls):
        names = [member.name for member in cls] 
        return names
    
    def get_by_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        return None
    