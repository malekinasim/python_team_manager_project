from services.team_managers import TeamManager
from models.enums.team_type import TeamType

class MenuUI:
    def __init__(self, manager: TeamManager):
        self.manager = manager
    
    def _manage_options(self,choice):
            if choice == "1":
                name = input("Team name: ")
                team_type = input("Team type (boy/girl): ").strip().lower()
                if team_type not in [t.value for t in TeamType]:
                    print("Invalid team type! Choose 'boy' or 'girl'.")
                else:
                    fee = float(input("Participation fee(if wasn't paid enter 0): "))
                    team=self.manager.add_team(name,team_type, fee)
                    if team:
                            print(team)
                    else:
                            print("Team not found!")
            elif choice == "2":
                team_id = int(input("Enter team ID to search: "))
                team = self.manager.find_by_id(team_id)
                if team:
                    print(team)
                else:
                    print("Team not found!")
            elif choice == "3":
                team_type = input("which type of teams you want to see?\nTeam type (boy/girl): ").strip().lower()
                teams = self.manager.find_all_by_team_type(team_type=team_type)
                if(teams is None or len(teams)==0):
                    print(f"No teams found with type {team_type}")
                else:
                    print(f"\n---{team_type}'s Hockey Tournament Teams ---\n")
                    for team in teams:
                        print(team)
            elif choice == "4":
                teams = self.manager.find_all()
                if(teams is None or len(teams)==0):
                    print("No teams found")
                else:   
                    print("\n--- Hockey Tournament Teams ---\n")
                    for team in teams:
                        print(team)
            elif choice == "5":
                team_id = int(input("Enter team ID to update: "))
                team = self.manager.find_by_id(team_id)
                if team:
                    print(f"selected team info id: \n{team}")
                    name = input("New team name: ") or team.get_name()
                    team_type = input("New team type (boy/girl): ") or team.get_team_type()
                    fee = input("New participation fee: ") or team.get_fee_amount()
                    self.manager.update_team(team,name,team_type.strip().lower(),float(fee) )
                else:
                    print("Team not found!") 
            elif choice == "6":
                team_id = int(input("Enter team ID to remove: "))
                self.manager.remove_entity(team_id)
                
            elif choice == "7": 
                team_id = int(input("Enter team ID to cancel participation: "))
                self.manager.cancel_team(team_id)
                
            elif choice == "8": 
                return False
            else:
                print("Invalid option!")
            return True
        
    def show_menu(self):
        while True:
            print("\n--- Hockey Tournament Teams Management ---")
            print("1. Add a new team")
            print("2. read individual teams id")
            print("3. read teams (girl/boy)")
            print("4. read all teams")
            print("5. update a team")
            print("6. remove a team")
            print("7. Cancel a team's participation") 
            print("8. Exit")            
            choice = input("Choose an option: ")
            result=self._manage_options(choice)
            if(not result):
                break            
