'''Defines common time units used in spell casting.'''

from enum import Enum

class CommonTime(Enum):
    '''Common time units used for casting times and durations in spells.'''
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
