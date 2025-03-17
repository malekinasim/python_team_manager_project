from models.basic_types.team_member import TeamMember
from models.enums.team_type import TeamType
from models.basic_types.basic_type import BasicObject
class Team(BasicObject):       
    def __init__(self,name,type,code,id=None,
            fee_paid=False,fee_amount=0,
            cancel_date=None,
            created_date=None):
        super().__init__(code,created_date,id)
        self.set_name(name)
        self.set_type(type)
        self._fee_paid = fee_paid
        self._fee_amount = fee_amount
        self._cancel_date=cancel_date
    
    def set_name(self,name):
        if(name is None):
            raise ValueError("the team name is required")   
        self._name=name
    
    def set_type(self,type):
        team_type=TeamType.get_by_value(type)
        if(team_type is None):
            raise ValueError("the team type is incorrect")
        else:
            self._team_type=team_type
        
    # def set_members(self,team_members):
    #     if team_members is None or not isinstance(team_members,list) or len(team_members)==0:
    #         return []
    #     for member in team_members:
    #         if not isinstance(member,TeamMember):
    #             raise ValueError("the team member is not valid")
    #         self._team_members=team_members
        
    def set_canceled_date(self,cancel_date):
        self._cancel_date=cancel_date
        
    def set_fee_amount(self,fee_amount):
        self._fee_amount=fee_amount
        
    def set_fee_paid(self,fee_paid):
        self._fee_paid=fee_paid
    
    def get_name(   self):
        return self._name
    
    def get_team_type(self):
        return self._team_type.value
    
    def get_fee_paid(self):
        return self._fee_paid
    def get_fee_amount(self):
        return self._fee_amount 
    
    # def get_team_members(self):
    #     return self._team_members 
    
    def get_cancel_date(self):
        return self._cancel_date
    
    def __str__(self):
        maximum=max(len(f"Name: {self._name}")
         ,len(f"Id: {self._id}")
         ,len(f"Code: {self._code}")
         ,len(f"Team Type: {self._team_type.value}")
         ,len(f"Fee Paid: {'YES' if self._fee_paid else 'NO'}")
         ,len(f"Fee Amount: {self._fee_amount:.2f}")
         ,len(f"Cancel Date: {self._cancel_date if self._cancel_date else 'Active'}"),
         len(f"created at: {self._created_date}"))
    
        
        return Team.format_columns(
                Team.format_columns(f"Id: {self._id}",
                                    f"Code: {self._code}",
                                    sep='\t',ljust=maximum),
                Team.format_columns(f"Name: {self._name}",
                                    f"Team Type: {self._team_type.value}",
                                    sep='\t',ljust=maximum), 
                Team.format_columns(f"Fee Paid: {'YES' if self._fee_paid else 'NO'}", 
                                    f"Fee Amount: {self._fee_amount:.2f}",
                                    sep='\t',ljust=maximum), 
                Team.format_columns(f"created at: {self._created_date}",
                                    f"Cancel Date: {self._cancel_date if self._cancel_date else 'Active'}",
                                    sep='\t',ljust=maximum)
                ,sep='\n'
                )+"\n"
               
    
    @staticmethod
    def get_table_name():
        return 'teams'
    
    @staticmethod
    def get_code_column_name():
        return 'team_id'
    
    def code_entity(self):
        return Team.format_columns(self._id,self._code,self._name,
                                   self._team_type.value,self._fee_paid, 
                                   self._fee_amount,self._cancel_date,self._created_date,sep=',')

    @staticmethod
    def decode_entity(str):
        if str is None or len(str)==0:
            return None
        arr=str.split(',')
        id=int(arr[0])
        code=arr[1]
        name=arr[2]
        team_type=arr[3]
        fee_paid=bool(arr[4])
        fee_amount=float(arr[5])
        if arr[6]  and arr[6]!='None' :
            cancel_date=arr[6]
        else:
            cancel_date=None
        if arr[7]  and arr[7]!='None' :
            created_date=arr[7]
        else:
            created_date=None
        return Team(name,team_type,code,id,fee_paid,fee_amount,cancel_date,created_date)
        