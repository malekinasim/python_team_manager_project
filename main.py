from utils.repositories.storage_factory import StorageFactory
from controllers.team_managers import TeamManager
from utils.repositories.storage_type import StorageType
from models.basic_types.team import Team
from views.userInterface import UserInterface 
import  utils.file_util as file_util


def get_storage_choice():
    print("Select storage type:")
    print("1. Store in text file (default)")
    print("2. Store in database (SQLite)")
    choice = input("Please choose an option (1 or 2): ")
    
    if choice == "2":
        return StorageType.DB
    return StorageType.TEXT  # Default value

if __name__ == "__main__":
    team_ddl_query = '''CREATE TABLE IF NOT EXISTS teams (
    name TEXT NOT NULL,
    team_type TEXT NOT NULL,
    code TEXT NOT NULL,
    id INTEGER PRIMARY KEY NOT NULL,
    fee_paid INTEGER NOT NULL,  -- 0 = False, 1 = True
    fee_amount REAL NOT NULL,
    cancel_date TEXT,  -- YYYY-MM-DD
    created_date TEXT  -- YYYY-MM-DD
    );'''
    
    fee_membership_ddl_query = '''CREATE TABLE IF NOT EXISTS team_membership_fee (
    id INTEGER PRIMARY KEY NOT NULL,
    code TEXT NOT NULL,
    fee_paid INTEGER NOT NULL,  -- 0 = False, 1 = True
    fee_amount REAL NOT NULL,
    start_date TEXT,  -- YYYY-MM-DD
    end_date TEXT,  -- YYYY-MM-DD
    created_date TEXT  -- YYYY-MM-DD
    );'''
    
    storage_type = get_storage_choice()
    
    if storage_type == StorageType.DB:
        team_storage = StorageFactory.getStorage(
            storage_name=StorageType.DB.name,
            config={'DB_NAME': 'hockey_cup.db', 'PRE_QUERY': (team_ddl_query,fee_membership_ddl_query)},
            entity_class=Team
        )
    else:
        team_storage = StorageFactory.getStorage(
            storage_name=StorageType.TEXT.name,
            config={'storage_file_dir': 'data\\filestorage'},
            entity_class=Team
        )
    try:
        last_fee=file_util.read_file('data\\filestorage\\MembershipFee.txt')
    except Exception as e:
        last_fee=None
    
    if(last_fee is None or  last_fee==''):
        while True:
            try:
                membershipFee=float(input("please enter the hockey Tournament  membership fee:"))
                file_util.write_file('data\\filestorage\\MembershipFee.txt',str(membershipFee))
                break
            except ValueError as e:
                print("you entered invalid membership fee amount value!!")
    ui = UserInterface(TeamManager(team_storage))
    ui.show_menu()
    

    