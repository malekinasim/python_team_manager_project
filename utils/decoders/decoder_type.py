# This class `DecoderType` defines an enumeration for different types of decoders along with their
# corresponding decoder classes.
from typing import Type,TypeVar,Optional
from models.enums.enum_type import EnumType
from utils.decoders.db_record_decoder import DbRecordDecoder
from utils.decoders.json_decoder import JsonDecoder
from utils.decoders.string_decoder import StringDecoder
from utils.decoders.decoder import Decoder 


''' using TypeVar to create a generic type variable T that is bound to the Decoder class using the bound parameter.
This means that T can be any subclass of Decoder. This is useful when you want to create a method or function that can accept any decoder type.
For example, the get_by_value method returns a decoder class that is a subclass of Decoder.
This allows for more flexibility and type safety in your code.'''  
T=TypeVar('T',bound=Decoder)
class DecoderType(EnumType):
    JSON = ('json',JsonDecoder)
    STR = ('string',StringDecoder)
    DB_RECORD=('db_record',DbRecordDecoder)
    def __init__(self, decoder_type: str,decoder_class:type[T]):
        super().__init__(decoder_type)
        self.decoder_type = decoder_type   # e.g., 'json_file'
        self.decoder_class = decoder_class  # e.g., JsonFileStorage
    
    @classmethod
    def get_by_name(cls, name)-> Optional[Type[T]]:
        for member in cls:
            if member.name == name:
                return member.decoder_class
        return None
    
    