import sqlite3
def create_connection(dbName):
    return sqlite3.connect(dbName)

def create_table(connection,query):
    connection.execute(query)
    connection.commit()
def select_entity_by_id(connection,table_name,id_column_name,id):
    query=f"SELECT * FROM {table_name}  WHERE {id_column_name} = ?"
    cursor= connection.execute(query , (id,))
    
    return cursor.fetchone()

def select_all_entity(connection,table_name):
    cursor= connection.execute(f"SELECT * FROM {table_name}")
    return cursor

def filter_entity(connection, table_name,filters):
    query=f"SELECT * FROM {table_name} WHERE "
    i=1
    values=[]
    for getter_field_method,filter_value in filters.items():
        parts=getter_field_method.rsplit('get_',-1)
        
        filed_name=parts[1] if len(parts)>1 else getter_field_method
        if(i<len(filters)):
            if(filter_value is not None):
               query+=f"{filed_name} = ? AND "
            else:
               query+=f"{filed_name} is null AND "
        else:
            if(filter_value is not None):
               query+=f"{filed_name} = ? "
            else:
               query+=f"{filed_name} is null "
        
        if(filter_value is not None ):
            if(isinstance(filter_value,bool)):
                values.append(1 if filter_value==True else 0)
            else :
                values.append(filter_value) 
        i+=1
    
    if(len(values)==0):
         cursor= connection.execute(query)
    else:
       cursor= connection.execute(query , (*values,))
    return cursor

def delete_entity_by_id(connection,table_name,id_column_name,id):
    connection.execute(f'''DELETE FROM {table_name}
                    WHERE {id_column_name} = ?''', (id,))
    connection.commit()

def update_entity_by_id(connection,table_name,id,id_column_name,column_name_list,column_value_list):
    query=f"UPDATE {table_name} set"
    id_index=-1
    for i,column_name in enumerate(column_name_list):
        if(column_name!=id_column_name):
            if(i+1<len(column_name_list)):
                query+=f" {column_name}=?, "
            else:
                query+=f" {column_name}=? "
        else:
            id_index=i
    if(id_index>=0):
        del column_value_list[id_index]
    for i,value in enumerate(column_value_list):
        if(isinstance(value,bool)):
            column_value_list[i]=0 if value==False else 1
        elif isinstance(value, (float)):
            column_value_list[i]=float(column_value_list[i])
    cursor=connection.cursor()
    connection.execute(f'''{query} WHERE {id_column_name} = ?''', (*column_value_list, id))
    connection.commit()

def save_entity(connection,table_name,column_name_list,column_value_list):
    query_part1=f"INSERT INTO {table_name}("
    query_part2=") VALUES("
    for i,column_name in enumerate(column_name_list):
        if(i+1<len(column_name_list)):
            query_part1+=f"{column_name}, "
            query_part2+="?, "
        else:
            query_part1+=f"{column_name} "
            query_part2+="? "
    
    query=query_part1+query_part2+")"
    
    connection.execute(query,(*column_value_list,))
    connection.commit()
