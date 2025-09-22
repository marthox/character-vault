from enum import Enum

class CommonTime(Enum):
    # Instantaneous
    INSTANTANEOUS = "instantaneous"
    
    # Standard Casting Times
    ACTION = "action"
    BONUS_ACTION = "bonus action"
    REACTION = "reaction"
    
    # Time base casting times
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    

