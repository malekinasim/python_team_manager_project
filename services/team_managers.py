from utils.repositories.storage import Storage
from models.basic_types.team import Team
from services.basic_manager import BasicManager
from datetime import datetime
class TeamManager(BasicManager[Team]):
    def __init__(self, storage: Storage[Team]):
        super().__init__(storage)
    

    def find_all_by_team_type(self,team_type):
        return self._storage.find_all_by_properties({
            "get_team_type":team_type
        })
        
    def find_all_fee_paid_teams(self):
        return self._storage.find_all_by_properties({
            "get_team_type":True
        })
    
    def remove_entity(self, team_id):
        team = self._storage.find_by_id(team_id)  
        
        if team:
            super().remove_entity(team_id)
            print(f"the team {team.get_name()} has been removed from the tournament. ")
            print(team)
        else:
            print("Team not found!")
    
    def update_team(self, entity:Team,name, type, fee_amount=0):
        entity.set_name(name)
        entity.set_type(type)
        entity.set_fee_amount(fee_amount)
        if(fee_amount!=0):
            entity.set_fee_paid(True)
        else:
            entity.set_fee_paid(False)
        return super().update_entity(entity)
    
    def add_team(self, name, type, fee_amount=0):
        fee_paid=False
        if(fee_amount!=0):
            fee_paid=True
        created_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id=0
        try:
            list=self._storage.find_all()
            id=len(list)+1
            code=f"TEAM-{len(list)+1}"
        except Exception as e:
            id=1
            code=f"TEAM-{1}"
    
        team =Team(name=name,type=type,code=code,id=id,
            fee_paid=fee_paid,fee_amount=fee_amount,created_date=created_date)
        
        super().save_entity(team)
        
        return team

    def cancel_team(self, team_id):
        team = self._storage.find_by_id(team_id)  
        if team:
            team.set_canceled_date(datetime.now().strftime("%Y-%m-%d")) 
            self._storage.update_entity(team)
            print(f"the participation of team  {team.get_name()} in the tournament has been canceled.")
            print(team)
        else:
            print("Team not found!")
    
    def team_count(self):
        teams=self._storage.find_all() 
        return len(teams)
    
     
        