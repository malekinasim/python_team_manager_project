import sqlite3
def create_connection(dbName):
    return sqlite3.connect(dbName)

def create_table(connection,query):
    connection.execute(query)
    connection.commit()
def select_entity_by_id(connection,table_name,id,id_column_name):
    cursor= connection.execute(f'''SELECT * FROM {table_name}
                            WHERE {id_column_name} = ?''', (id,))
    
    return cursor.fetchone()

def select_all_entity(connection,table_name):
    cursor= connection.execute(f"SELECT * FROM {table_name}")
    return cursor

def delete_entity_by_id(connection,table_name,id,id_column_name):
    connection.execute(f'''DELETE FROM {table_name}
                    WHERE {id_column_name} = ?''', (id,))
    connection.commit()

def update_entity_by_id(connection,table_name,id,id_column_name,column_name_list,column_value_list):
    query=f"UPDATE {table_name} set"
    for i,column_name in enumerate(column_name_list):
        if(i+1<len(column_name_list)):
            query+=f" {column_name}=?, "
        else:
            query+=f" {column_name}=? "
        
    connection.execute(f'''{query} WHERE {id_column_name} = ?''', (*column_value_list, id))
    connection.commit()

def save_entity_by_id(connection,table_name,column_name_list,column_value_list):
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
    connection.commit
