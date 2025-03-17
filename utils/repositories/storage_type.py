from models.enums.enum_type import EnumType
from utils.repositories.db_storage import Storage
from utils.repositories.db_storage import DBStorage
from utils.repositories.json_file_storage import JsonFileStorage
from utils.repositories.text_file_storage import TextFileStorage
from typing import Type,TypeVar,Optional

T=TypeVar("T",bound=Storage)
class StorageType(EnumType):
    JSON = ('json_file',JsonFileStorage)
    TEXT = ('text_file',TextFileStorage)
    DB=('database',DBStorage)
    
    T=TypeVar("T",bound=Storage)

    
    @classmethod
    def get_by_name(cls, name)->Optional[Type[T]]:
        for member in cls:
            if member.name== name:
                return member.value[1]  # Return the corresponding Storage class
        return None
    
    