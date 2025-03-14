from modules.enum_types.gender import TeamType
from modules.basic_type.team_member import TeamMember
class Team:
    
    def __init__(self,name,type,code,
            fee_paid=False,fee_amount=0,fee_paid_date=None,
            team_members=None):
        self._set_name(name)
        self._set_code(code)
        self._set_type(type)
        self._fee_paid = fee_paid
        self._fee_amount = fee_amount
        self._fee_paid_date = fee_paid_date
        self.set_members(team_members)
    
    def _set_name(self,name):
        if(name is None):
            raise ValueError("the team name is required")   
        self._name=name
        
    def _set_code(self,code):
        if(code is None):
            raise ValueError("the team name is required")   
        self._code=code

    def _set_type(self,type):
        team_type=TeamType.getEnum(type)
        if(team_type is None):
            raise ValueError("the team type is incorrect")
        else:
            self._team_type=team_type
        
    def set_members(self,team_members):
        if team_members is None or not isinstance(team_members,list) or len(team_members)==0:
            return []
        for member in team_members:
            if not isinstance(member,TeamMember):
                raise ValueError("the team member is not valid")
            self._team_members=team_members
        
    
    def get_name(self):
        return self._name
    
    def get_code(self):
        return self._code
    
    def get_code(self):
        return self._team_type.value
    
    def get_fee_paid(self):
        return self._fee_paid
    def get_fee_amount(self):
        return self._fee_amount 
    
    def get_fee_paid_date(self):
        return self._fee_paid_date 
    
    def get_team_members(self):
        return self._team_members 
        