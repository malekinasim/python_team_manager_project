from utils.repositories.storage import Storage
import os
from utils.file_util import read_file_lines,write_file,append_file
from models.basic_types.team import Team
from typing import TypeVar,Generic,Type
from models.basic_types.basic_type import BasicObject
from utils.decoders.string_decoder import StringDecoder
T=TypeVar('T',bound=BasicObject)
class TextFileStorage(Storage,Generic[T]):
    _storage_file_path=None
    _entity_class=None
    
    """This Python class provides methods for managing entities stored in a text file.
        :param cls: In the provided code snippet, `cls` refers to the class itself, which is a common
        convention in Python to refer to the class within class methods. It is used to access class
        variables and methods within the class itself
        :param config: The `config` parameter is expected to be a tuple containing configuration details
        for the Text file Storage. It should include a key-value pair where the key is `'storage_file_dir'`
        specifying the directory where the data file will be stored
        :type config: tuple
        """
    
    @classmethod
    def _create_instance(cls, config: dict,entity_class:T):
        if 'storage_file_dir' not in config :
            raise Exception('''the configuration for Text file Storage is invalid ,
                            storage_file_dir is required''')
        cls._storage_file_path=os.path.join(config.get('storage_file_dir'),f'data_{entity_class.__qualname__}.text')
        cls._entity_class=entity_class
        return cls[entity_class]
    @classmethod    
    def find_by_id(cls, id)->T:
        lines=read_file_lines(cls._storage_file_path)
        for line in lines:
            if( line.strip()!=''):
                entity=StringDecoder[T].decode(line, cls._entity_class)
                if entity and entity.get_id()==id:
                    return entity
        return None

    @classmethod 
    def save_entity(cls, data:T):
        if not os.path.exists(cls._storage_file_path):
            write_file(cls._storage_file_path,data.code_entity())
        else:
            append_file(cls._storage_file_path,data.code_entity())
    
    @classmethod
    def find_all_by_properties(cls,filter: dict)->list[T]:
        lines=read_file_lines(cls._storage_file_path)
        result=[]
        for line in lines:
            if( line.strip()!=''):
                entity=StringDecoder[T].decode(line, cls._entity_class)
                if entity:
                    is_filter=False
                    for getter_method,filter_value in filter.items():
                        if(getattr(entity, getter_method)()!=filter_value):
                            is_filter=True
                            break
                    if(not is_filter):
                        result.append(entity)
        return result
    @classmethod
    def find_all(cls)->list[T]:
        lines=read_file_lines(cls._storage_file_path)
        result=[]
        for line in lines:
            if( line.strip()!=''):
                entity=StringDecoder[T].decode(line, cls._entity_class)
                if entity:
                    result.append(entity)
        return result
    
    @classmethod
    def update_entity(cls, data:T):
        lines=read_file_lines(cls._storage_file_path)
        updated=False
        for i,line in enumerate(lines):
            if( line.strip()!=''):
                entity=StringDecoder[T].decode(line, cls._entity_class)
                if entity is not None and entity.get_id()==data.get_id():
                    lines[i]=data.code_entity()
                    updated=True
                    break
            
        if(updated):  
            write_file(cls._storage_file_path,'\n'.join(lines))
        else:
            raise Exception(f'entity with id={entity.get_id()}  not found')
    
    @classmethod
    def delete_by_id(cls, id):
        lines=read_file_lines(cls._storage_file_path)
        
        for i,line in enumerate(lines):
            if( line.strip()!=''):
                entity=StringDecoder[T].decode(line, cls._entity_class)
                if entity is not None and entity.get_id()==id:
                    del lines[i]
                    break
        write_file(cls._storage_file_path,'\n'.join(lines))