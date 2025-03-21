from controllers.team_managers import TeamManager
from models.enums.team_type import TeamType
import utils.file_util as file_util

class UserInterface:
    def __init__(self, team_manager: TeamManager):
        self.team_manager = team_manager

    def _get_valid_team_id(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid ID! Please enter a numeric value.")

    def _get_valid_team_type(self, prompt: str,current_type:None) -> str:
        while True:
            team_type = input(prompt).strip().lower()
            if(team_type=='' and current_type is not None):
                return current_type
            for t in TeamType:
                if(team_type == t.value): 
                    return team_type  
            print("Invalid team type! Choose 'boy' or 'girl'.")

    def _get_valid_fee(self, last_membership_fee: float,current_fee) -> float:
        while True:
            try:
                if (current_fee is not None and current_fee>0):
                    fee = float(input(f"The last membership fee is: {last_membership_fee:,.2f}\nthis team currently paid {current_fee} ,so the new paid Participation fee (enter 0 if unpaid): "))
                else:
                    fee = float(input(f"The last membership fee is: {last_membership_fee:,.2f}\nParticipation fee (enter 0 if unpaid): "))
                if fee > last_membership_fee:
                    print(f"Fee must bet equal  or less than {last_membership_fee:,.2f}!")
                else:
                    if fee < last_membership_fee:
                        print(f"Remaining fee to collect: {(last_membership_fee - fee):,.2f}")
                    return fee
            except ValueError:
                print("Invalid amount! Enter a numeric value.")

    def _print_teams(self, teams):
        active_teams = [team for team in teams if team.get_cancel_date() is None]
        passive_teams = [team for team in teams if team.get_cancel_date() is not None]
        
        if active_teams:
            print("\n----- Active Teams -----\n")
            for team in active_teams:
                print(team)
        
        if passive_teams:
            print("\n----- Cancelled Teams -----\n")
            for team in passive_teams:
                print(team)
    
    def add_team(self):
        name = input("Team name: ")
        team_type = self._get_valid_team_type("Team type (boy/girl): ",None)
        last_membership_fee = float(file_util.read_file('data/filestorage/MembershipFee.txt'))
        fee = self._get_valid_fee(last_membership_fee,None)
        team = self.team_manager.add_team(name, team_type, fee, last_membership_fee)
        if team:
            print(team)
        else:
            print("Team not found!")

    def find_team_by_id(self):
        team_id = self._get_valid_team_id("Enter team ID to search: ")
        team = self.team_manager.find_by_id(team_id)
        if team:
            print(team)
        else:
            print("Team not found!")

    def find_teams_by_type(self):
        team_type = self._get_valid_team_type("Which type of teams do you want to see? (boy/girl): ",None)
        teams = self.team_manager.find_all_by_team_type(team_type)
        if not teams:
            print(f"No teams found with type {team_type}.")
        else:
            print(f"\n--- {team_type.capitalize()} Hockey Tournament Teams ---\n")
            self._print_teams(teams)

    def find_all_teams(self):
        teams = self.team_manager.find_all()
        if not teams:
            print("No teams found.")
        else:
            print("\n--- Hockey Tournament Teams ---\n")
            self._print_teams(teams)

    def update_team(self):
        team_id = self._get_valid_team_id("Enter team ID to update: ")
        team = self.team_manager.find_by_id(team_id)
        if team:
            if team.get_cancel_date():
                print(f"This team  ({team.get_name()}) was canceled on {team.get_cancel_date()}. Cannot update.")
                return
            print(f"Current team info: {team}")
            print("\n--- Skip the input to keep the current value ---\n")
            
            name = input(f"current name is ({team.get_name()}) the New team name : ") 
            if(name is None or name.strip()==''):
                name=team.get_name()
            
            team_type = self._get_valid_team_type(f"current team type  is ({team.get_team_type()}) New team type: ",team.get_team_type())
                
            last_membership_fee = float(file_util.read_file('data/filestorage/MembershipFee.txt'))
            fee = self._get_valid_fee(last_membership_fee,team.get_fee_amount())
            self.team_manager.update_team(team, name, team_type, fee,last_membership_fee)
        else:
            print("Team not found!")

    def remove_team(self):
        team_id = self._get_valid_team_id("Enter team ID to remove: ")
        self.team_manager.remove_entity(team_id)

    def cancel_team(self):
        team_id = self._get_valid_team_id("Enter team ID to cancel participation: ")
        self.team_manager.cancel_team(team_id)

    def show_statistics(self):
        all_team_count, fee_paid_count, active_count, active_paid_count = self.team_manager._show_teams_statistics()
        print(f"Total Teams: {all_team_count}\nTeams that Paid Fee: {fee_paid_count} ({(fee_paid_count / all_team_count * 100) if all_team_count else 0:.2f}%)")
        print(f"Active Teams: {active_count}\nActive Teams that Paid Fee: {active_paid_count} ({(active_paid_count / active_count * 100) if active_count else 0:.2f}%)")
    
    def change_membership_fee(self):
        while True:
            try:
                fee = float(input("Enter new membership fee: "))
                file_util.write_file('data\\filestorage\\MembershipFee.txt',str(fee))
                break
            except ValueError:
                print("Invalid value! Enter a numeric fee.")
    def manage_options(self, choice):
        options = {
            1: self.add_team,
            2: self.find_team_by_id,
            3: self.find_teams_by_type,
            4: self.find_all_teams,
            5: self.update_team,
            6: self.remove_team,
            7: self.cancel_team,
            8: self.show_statistics,
            9: self.change_membership_fee
        }
        action=options.get(choice)
        if(action):
            action()
        else:
            print("invalid option please try again")
        
    def show_menu(self):
        while True:
            try:
                print("\n--- Hockey Tournament Teams Management ---")
                print("1. Add a new team.")
                print("2. View a team by ID")
                print("3. View teams by category (boys/girls).")
                print("4. List all teams.")
                print("5. Update a team.")
                print("6. Remove a team.")
                print("7. Cancel a team’s participation.") 
                print("8. show statics")
                print("9. Change membership fee.")
                print("10. Exit")            
                choice = int(input("Choose an option: "))
                if(choice==10):
                    break
                elif choice>10:
                    print("invalid options please try again")
                    continue 
                else:
                    self.manage_options(choice)
            except ValueError as e:
                print("invalid options please try again")