from modules.enum_types.gender import Gender
from modules.enum_types.team_role_type import TeamRoleType
from modules.basic_type.basic_type import BasicType

class TeamMember(BasicType):
    def __init__(self, name, age, gender,roles):
        self._set_name(name)
        self._set_age(age)
        self._set_gender(gender)
        self._set_roles(roles) 
        
    def _set_name(self,name):
        if(name is None):
            raise ValueError("name must be non empty value")
        self._name=name
        
    def _set_age(self, age):
        if (not  isinstance(age,int) or age < 0 ) :
            raise ValueError("age must be positive integer") 
        self._age = age
    
    def _set_gender(self,gender):
        gender_type=Gender.get_by_value(gender)
        if( gender is None):
            raise ValueError("invalid gender type for team member")
        self._gender_type=gender_type
    
    def _set_roles(self,roles):
        if (not isinstance(roles,list) or len(roles)==0):
            raise ValueError("roles must be a non empty list")
        role_types=[]
        for role in roles:
            role_type=TeamRoleType.get_by_value(role)
            if(role_type is None):
                raise ValueError("invalid role type for team member")
            role_types.append(role_type)
            
        self._role_types=role_types
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_gender(self):
        return self._gender_type.value
    
    def get_roles(self):
        return [role for role in self._role_types.value]