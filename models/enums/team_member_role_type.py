from models.enums.enum_type import EnumType
class TeamMemberRoleType(EnumType):
    COACH = 'coach'
    COACH_ASSISTANCE = 'coach_assistance'
    PLAYER = 'player'
    GOALKEEPER = 'goalkeeper'