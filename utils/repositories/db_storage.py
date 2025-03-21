from utils.repositories.storage import Storage
from typing import Generic, TypeVar
from models.basic_types.basic_type import BasicObject
from utils.db_util import create_connection,filter_entity ,create_table, save_entity as save_entity_to_db,update_entity_by_id,delete_entity_by_id, select_entity_by_id, select_all_entity
from utils.decoders.db_record_decoder import DbRecordDecoder
from enum import Enum
T = TypeVar('T', bound=BasicObject)

class DBStorage(Storage, Generic[T]):
    __connection = None
    __entity_class = None
    
    @classmethod
    def create_instance(cls, config: dict,entity_class:T):
        if 'DB_NAME' not in config or 'PRE_QUERY' not in config:
            raise Exception('''The configuration for database Storage is invalid. 
                            It is required to have a DB_NAME key in the input config
                            and a PRE_QUERY key. The PRE_QUERY key should be a :: separated string of queries or a list of strings.''')
        cls.__entity_class=entity_class   
        if cls.__connection is None:
            cls.__connection = create_connection(dbName=config['DB_NAME'])
        
        # If PRE_QUERY is a string of queries separated by '::', we split it, otherwise use it as is
        if isinstance(config['PRE_QUERY'], str):
            queryset = config['PRE_QUERY'].split('::') if '::' in config['PRE_QUERY'] else [config['PRE_QUERY']]
        else:
            queryset = config['PRE_QUERY']
        
        for query in queryset:
            create_table(cls.__connection, query)
        return cls[entity_class]
    
    @classmethod
    def find_by_id(cls, id) -> T:
        row = select_entity_by_id(cls.__connection, cls.__entity_class.get_table_name(), cls.__entity_class.get_id_column_name(), id)
        if row:
            return DbRecordDecoder[T].decode(row,cls.__entity_class)
        return None

    @classmethod
    def find_all(cls) -> list[T]:
        rows = select_all_entity(cls.__connection, cls.__entity_class.get_table_name())
        list=[]
        for row in rows:
            entity=DbRecordDecoder[T].decode(row,cls.__entity_class) 
            if(entity is not None):
                list.append(entity)
        return list
    
    @classmethod
    def find_all_by_properties(cls,filter: dict)->list[T]:
        rows = filter_entity(cls.__connection, cls.__entity_class.get_table_name(),filter)
        list=[]
        for row in rows:
            entity=DbRecordDecoder[T].decode(row,cls.__entity_class) 
            if(entity is not None):
                list.append(entity)
        return list
    @classmethod
    def delete_by_id(cls, id):
        delete_entity_by_id(cls.__connection, cls.__entity_class.get_table_name(), cls.__entity_class.get_id_column_name(), id)
    
    @classmethod
    def __get_entity_attributes(cls,data):
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
        column_names,column_values=cls.__get_entity_attributes(data)
        update_entity_by_id(cls.__connection,cls.__entity_class.get_table_name(),data.get_id(),cls.__entity_class.get_id_column_name(),column_names, column_values)
    
    @classmethod 
    def save_entity(cls, data:T):
        column_names,column_values=cls.__get_entity_attributes(data)
        return save_entity_to_db(cls.__connection,
                        cls.__entity_class.get_table_name(),
                        column_names, 
                        column_values)
    