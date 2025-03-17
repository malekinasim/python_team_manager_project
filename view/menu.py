from services.team_managers import TeamManager
from models.enums.team_type import TeamType

class MenuUI:
    def __init__(self, team_manager: TeamManager):
        self.team_manager = team_manager
    def _print_teams(self,teams):
        active_teams=[team for team in teams if team.get_cancel_date() is None]
        passive_teams=[team for team in teams if team.get_cancel_date() is not None]
        if(active_teams and len(active_teams)!=0):
            print("-----Active teams:-----\n")
            for team in active_teams:
                print(team)
        if(passive_teams and len(passive_teams)!=0):
            print("-----Cancelled teams:-----\n")
            for team in passive_teams:
                print(team)
                
                

        
                
    def _manage_options(self,choice):
            if choice == "1":
                name = input("Team name: ")
                team_type = input("Team type (boy/girl): ").strip().lower()
                if team_type not in [t.value for t in TeamType]:
                    print("Invalid team type! Choose 'boy' or 'girl'.")
                else:
                    fee = float(input("Participation fee(if wasn't paid enter 0): "))
                    team=self.team_manager.add_team(name,team_type, fee)
                    if team:
                            print(team )
                    else:
                            print("Team not found!")
            elif choice == "2":
                team_id = int(input("Enter team ID to search: "))
                team = self.team_manager.find_by_id(team_id)
                if team:
                    print(team)
                else:
                    print("Team not found!")
            elif choice == "3":
                team_type = input("which type of teams you want to see?\nTeam type (boy/girl): ").strip().lower()
                teams = self.team_manager.find_all_by_team_type(team_type=team_type)
                if(teams is None or len(teams)==0):
                    print(f"No teams found with type {team_type}")
                else:
                    print(f"\n---{team_type}'s Hockey Tournament Teams ---\n")
                    self._print_teams(teams)
            elif choice == "4":
                teams = self.team_manager.find_all()
                if(teams is None or len(teams)==0):
                    print("No teams found")
                else:   
                    print("\n--- Hockey Tournament Teams ---\n")
                    self._print_teams(teams)
                    
            elif choice == "5":
                team_id = int(input("Enter team ID to update: "))
                team = self.team_manager.find_by_id(team_id)
                if team:
                    if(team.get_cancel_date() is None):
                        print(f"selected team info : \n{team}")
                        name = input("New team name: ") or team.get_name()
                        team_type = input("New team type (boy/girl): ") or team.get_team_type()
                        fee = input("New participation fee: ") or team.get_fee_amount()
                        self.team_manager.update_team(team,name,team_type.strip().lower(),float(fee) )
                    else:
                         print(f"your selected team info : \n{team}")
                         print(f"\n this team is canceled on {team.get_cancel_date()} you can't update canceled team data")
                else:
                    print("Team not found!") 
            elif choice == "6":
                team_id = int(input("Enter team ID to remove: "))
                self.team_manager.remove_entity(team_id)
                
            elif choice == "7": 
                team_id = int(input("Enter team ID to cancel participation: "))
                self.team_manager.cancel_team(team_id)
            elif choice == "8":
                all_team_count,fee_paid_team_count,active_team_count,active_fee_paid_team_count=self.team_manager._show_teams_statistics()
                print(f"Total Teams count : {all_team_count}")
                print(f"Total Teams that paid the fee count: {fee_paid_team_count}")
                print(f"Percentage of total teams that paid the fee: { round((fee_paid_team_count/all_team_count)*100,2) if all_team_count!=0 else 0:.2f}%")
                
                print(f"Total Active teams count :{active_team_count}")
                print(f"Total Active teams that paid the fee count  :{active_fee_paid_team_count}")
                print(f"Percentage of total active teams that paid the fee: {round((active_fee_paid_team_count/active_team_count)*100,2) if active_team_count!=0 else 0:.2f}%")
                
   
            elif choice == "9": 
                return False
            else:
                print("Invalid option!")
            return True
        
    def show_menu(self):
        while True:
            print("\n--- Hockey Tournament Teams Management ---")
            print("1. Add a new team")
            print("2. read individual teams id")
            print("3. read teams  by type(girl/boy)")
            print("4. read all teams")
            print("5. update a team")
            print("6. remove a team")
            print("7. Cancel a team's participation") 
            print("8. show statics")
            print("9. Exit")            
            choice = input("Choose an option: ")
            result=self._manage_options(choice)
            if(not result):
                break            
