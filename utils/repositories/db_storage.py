from utils.repositories.storage import Storage
from typing import Generic, TypeVar
from models.basic_types.basic_type import BasicObject
from utils.db_util import create_connection, create_table, save_entity_by_id,update_entity_by_id,delete_entity_by_id, select_entity_by_id, select_all_entity
from utils.decoders.db_record_decoder import DbRecordDecoder
from enum import Enum
T = TypeVar('T', bound=BasicObject)

class DBStorage(Storage, Generic[T]):
    _connection = None
    
    @classmethod
    def _create_instance(cls, config: dict,entity_class:T):
        if 'DB_NAME' not in config or 'PRE_QUERY' not in config:
            raise Exception('''The configuration for database Storage is invalid. 
                            It is required to have a DB_NAME key in the input config
                            and a PRE_QUERY key. The PRE_QUERY key should be a :: separated string of queries or a list of strings.''')
            
        if cls._connection is None:
            cls._connection = create_connection(dbName=config['DB_NAME'])
        
        # If PRE_QUERY is a string of queries separated by '::', we split it, otherwise use it as is
        if isinstance(config['PRE_QUERY'], str):
           queryset = config['PRE_QUERY'].split('::') 
        else:
           queryset =config['PRE_QUERY']
        
        for query in queryset:
            create_table(cls._connection, query)
        return cls[entity_class]
    
    @classmethod
    def find_by_id(cls, id) -> T:
        row = select_entity_by_id(cls._connection, T.get_table_name(), T.get_id_column_name(), id)
        if row:
            return DbRecordDecoder[T].decode(row,T)
        return None

    @classmethod
    def find_all(cls) -> list[T]:
        rows = select_all_entity(cls._connection, T.get_table_name())
        list=[]
        for row in rows:
            entity=DbRecordDecoder[T].decode(row,T) 
            if(entity is not None):
                list.append(entity)
        return list
    
    @classmethod
    def delete_by_id(cls, id):
        delete_entity_by_id(cls._connection, T.get_table_name(), T.get_id_column_name(), id)
    
    @classmethod
    def _get_entity_attributes(data):
        column_names=[]
        column_values=[]
        for field in data.__dict__.items():
            name=field[0]
            if(name.startswith('__')):
                continue
            if name.startswith('_'):
                name = name.lstrip('_')  

            value = field[1]
            if value is not None:  
                column_names.append(name)
                if(isinstance(value,Enum)):
                    value=value.value
                column_values.append(value)
        return column_names,column_values
    @classmethod
    def update_entity(cls, data:T):
        column_names,column_values=cls._get_entity_attributes(data)
        update_entity_by_id(cls._connection,T.get_table_name(),id,T.get_id_column_name(),column_names, column_values)
    
    @classmethod 
    def save_entity(cls, data:T):
        column_names,column_values=cls._get_entity_attributes(data)
        return save_entity_by_id(cls._connection,T.get_table_name(),id,T.get_id_column_name(),column_names, column_values)
    