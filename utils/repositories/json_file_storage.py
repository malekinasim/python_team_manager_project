from utils.repositories.storage import Storage
import os
import json
from utils.file_util import read_json_file,write_to_json_file,append_to_json_file
from utils.decoders.json_decoder import JsonDecoder 
from models.basic_types.team import Team
from typing import TypeVar,Generic
from models.basic_types.basic_type import BasicObject


T=TypeVar('T',bound=BasicObject)

class JsonFileStorage(Storage,Generic[T]):
    
    _storage_file_path=None
    
    @classmethod
    def _create_instance(cls, config: dict,entity_class:T):
        if 'storage_file_dir' not in config :
            raise Exception('''the configuration for Text file Storage is invalid ,
                            storage_file_dir is required''')
        cls._storage_file_path=os.path.join(config.get('storage_file_dir'),f'data_{entity_class.__qualname__}.text')
        return cls[entity_class]
    @classmethod    
    def find_by_id(cls, id)->T:
        json_array=read_json_file(cls._storage_file_path)
        for item in json_array:
            entity=JsonDecoder[T].decode(item,T)
            if entity and entity.get_id()==id:
                return entity
        return None

    @classmethod 
    def save_entity(cls, data:T):
        if not os.path.exists(cls._storage_file_path):
            write_to_json_file(cls._storage_file_path,[data])
        else:
            append_to_json_file(cls._storage_file_path,data)
    
    @classmethod
    def find_all(cls)->list[T]:
        json_array=read_json_file(cls._storage_file_path)
        result=[]
        for json in json_array:
            entity=JsonDecoder[T].decode(json,T)
            if entity:
                result.append(entity)
        return result
    
    @classmethod
    def update_entity(cls, data:T):
        json_array=read_json_file(cls._storage_file_path)
        
        updated=False
        for i,json in enumerate(json_array):
            entity=JsonDecoder[T].decode(json,T)
            if entity is not None and entity.get_id()==data.id:
                json_array[i]=data
                updated=True
                break
        if not updated:
            write_to_json_file(cls._storage_file_path,json_array)
        else:
            raise Exception(f'entity not  with id = {data.get_id()} not found to update')
    
    @classmethod
    def delete_by_id(cls, id):
        json_array=read_json_file(cls._storage_file_path)

        for i,json in enumerate(json_array):
            entity=JsonDecoder.decode(json,T)
            if entity is not None and entity.get_id()==id:
                del json_array[i]
                break
            
        write_to_json_file(cls._storage_file_path,json_array)
















