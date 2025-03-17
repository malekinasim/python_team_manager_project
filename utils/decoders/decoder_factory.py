from utils.decoders.decoder_type import DecoderType
from utils.decoders.decoder import Decoder
from typing import TypeVar,Generic
from models.basic_types.basic_type import BasicObject

T = TypeVar('T', bound=Decoder)
U=TypeVar("U", bound=BasicObject)
class DecoderFactory(Generic[T,U]): 
    '''this is a generic interface for storage'''
    _instances={}
    # Constructor for singleton subclass it's support that one instance of each decoder subclass is created
       
    @staticmethod
    def getDecoder(decoder_name,entity_class:U)->T:
        decoder_class=DecoderType.get_by_name(decoder_name)
        if( decoder_class is None ):
            raise ValueError("invalid decoder type ")
        return DecoderFactory._get_instance(entity_class)
    
    
    @staticmethod
    def _get_instance(decoder_class:T,entity_class:U):
        '''this method is used to get the instance of the storage class if this storage  
        currently doesn't have any instance it will create one and return it otherwise 
        it will return the already created instance'''
        return DecoderFactory._instances.setdefault(decoder_class,decoder_class[entity_class])
    