from utils.repositories.storage_factory import StorageFactory
from services.team_managers import TeamManager
from utils.repositories.storage_type import StorageType
from models.basic_types.team import Team
from view.menu import MenuUI 

if __name__ == "__main__":
    ddl_query = '''CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    code TEXT NOT NULL,
    type TEXT NOT NULL,
    fee_paid INTEGER NOT NULL,  -- 0 = False, 1 = True
    fee_amount REAL NOT NULL,
    fee_paid_date TEXT,  -- YYYY-MM-DD
    cancel_date TEXT,  -- YYYY-MM-DD
    create_date TEXT  -- YYYY-MM-DD
    );'''

    text_storage=StorageFactory.getStorage(storage_name=StorageType.TEXT.name,config={'storage_file_dir': 'data\\filestorage'},entity_class=Team)
    json_storage=StorageFactory.getStorage(storage_name=StorageType.JSON.name,config={'storage_file_dir': 'data\\filestorage'},entity_class=Team)
    db_storage=StorageFactory.getStorage(storage_name=StorageType.DB.name,config={'DB_NAME':'hockey_cup.db','PRE_QUERY':ddl_query},entity_class=Team)
    ui = MenuUI(TeamManager(text_storage))
    ui.show_menu()