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
        self.__fee_paid = fee_paid if isinstance(fee_paid,bool) else False if fee_paid==0  else True
        self.__fee_amount = fee_amount
        self.__cancel_date=cancel_date
    
    def set_name(self,name):
        if(name is None):
            raise ValueError("the team name is required")   
        self.__name=name
    
    def set_type(self,type):
        team_type=TeamType.get_by_value(type)
        if(team_type is None):
            raise ValueError("the team type is incorrect")
        else:
            self.__team_type=team_type
    
    def set_canceled_date(self,cancel_date):
        self.__cancel_date=cancel_date
        
    def set_fee_amount(self,fee_amount):
        self.__fee_amount=fee_amount
        
    def set_fee_paid(self,fee_paid):
        self.__fee_paid=fee_paid
    
    def get_name(   self):
        return self.__name
    
    def get_team_type(self):
        return self.__team_type.value
    
    def get_fee_paid(self):
        return self.__fee_paid
    
    def get_fee_amount(self):
        return self.__fee_amount 
    
    def get_cancel_date(self):
        return self.__cancel_date
    
    def __str__(self):
        maximum=max(len(f"Name: {self.__name}")
        ,len(f"Id: {self.get_id()}")
        ,len(f"Code: {self._code}")
        ,len(f"Team Type: {self.__team_type.value}")
        ,len(f"Fee Paid: {'YES' if self.__fee_paid else 'NO'}")
        ,len(f"Fee Amount: {self.__fee_amount:.2f}")
        ,len(f"Cancel Date: {self.__cancel_date if self.__cancel_date else 'Active'}"),
        len(f"created at: {self.get_cancel_date()}"))
    
        
        return Team.format_columns(
                Team.format_columns(f"Id: {self.get_id()}",
                                    f"Code: {self._code}",
                                    sep='\t',ljust=maximum),
                Team.format_columns(f"Name: {self.__name}",
                                    f"Team Type: {self.__team_type.value}",
                                    sep='\t',ljust=maximum), 
                Team.format_columns(f"Fee Paid: {'YES' if self.__fee_paid else 'NO'}", 
                                    f"Fee Amount: {self.__fee_amount:,.2f}",
                                    sep='\t',ljust=maximum), 
                Team.format_columns(f"created at: {self.get_created_date()}",
                                    f"Cancel Date: {self.__cancel_date if self.__cancel_date else 'Active'}",
                                    sep='\t',ljust=maximum)
                ,sep='\n'
                )+"\n"
    
    @staticmethod
    def get_table_name():
        return 'teams'
    
    @staticmethod
    def get_id_column_name():
        return 'id'
    
    def code_entity(self):
        return Team.format_columns(self.get_id(),self._code,self.__name,
                self.__team_type.value,self.__fee_paid, 
                self.__fee_amount,self.__cancel_date,self.get_created_date(),sep=',')

    @staticmethod
    def decode_entity(cod:str):
        if cod is None or len(cod)==0:
            return None
        arr=cod.split(',')
        if(len(arr)<7):
            return None
        id=int(arr[0])
        code=arr[1]
        name=arr[2]
        team_type=arr[3]
        fee_paid=False if arr[4]=='False' else True
        fee_amount=float(arr[5])
        if arr[6]  and arr[6]!='None' :
            cancel_date=arr[6]
        else:
            cancel_date=None
        if arr[7]  and arr[7]!='None' :
            created_date=arr[7]
        else:
            created_date=None
        return Team(name=name,type=team_type,code=code,
                    id=id,fee_paid=fee_paid,fee_amount=fee_amount,
                    cancel_date=cancel_date,created_date=created_date)