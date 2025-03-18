from utils.repositories.storage_factory import StorageFactory
from services.team_managers import TeamManager
from utils.repositories.storage_type import StorageType
from models.basic_types.team import Team
from view.menu import MenuUI 


def get_storage_choice():
    print("Select storage type:")
    print("1. Store in text file (default)")
    print("2. Store in database (SQLite)")
    choice = input("Please choose an option (1 or 2): ")
    
    if choice == "2":
        return StorageType.DB
    return StorageType.TEXT  # Default value

if __name__ == "__main__":
    ddl_query = '''CREATE TABLE IF NOT EXISTS teams (
    name TEXT NOT NULL,
    team_type TEXT NOT NULL,
    code TEXT NOT NULL,
    id INTEGER PRIMARY KEY NOT NULL,
    fee_paid INTEGER NOT NULL,  -- 0 = False, 1 = True
    fee_amount REAL NOT NULL,
    cancel_date TEXT,  -- YYYY-MM-DD
    created_date TEXT  -- YYYY-MM-DD
    );'''
    
    storage_type = get_storage_choice()
    
    if storage_type == StorageType.DB:
        storage = StorageFactory.getStorage(
            storage_name=StorageType.DB.name,
            config={'DB_NAME': 'hockey_cup.db', 'PRE_QUERY': ddl_query},
            entity_class=Team
        )
    else:
        storage = StorageFactory.getStorage(
            storage_name=StorageType.TEXT.name,
            config={'storage_file_dir': 'data\filestorage'},
            entity_class=Team
        )
    
    ui = MenuUI(TeamManager(storage))
    ui.show_menu()
