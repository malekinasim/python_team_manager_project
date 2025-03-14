from datetime import datetime
from  modules.basic_type.basic_type  import BasicType
class TeamMembershipFee(BasicType):

    def __init__(self,fee_amount:0):
        self._set_fee_amount(fee_amount)
        self._start_date=datetime.now()
        
    def _set_fee_amount(self,fee_amount): 
        if(fee_amount is None):
            raise ValueError("fee amount cannot be None")
        self.fee_amount=fee_amount
    
    def set_end_date(self,end_date):
        self.end_date=end_date
    
    def get_fee_amount(self):
        return self.fee_amount
    
    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date 
    
    def __str__(self):
       if(self.end_date is None):
           return f"the last fee amount for subscription is {self.fee_amount} that starts from {self.start_date} "
       return f"this fee amount for subscription is {self.fee_amount} that starts from {self.start_date} to {self.end_date}  "
    