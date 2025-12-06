'''
Defines the BaseClass model that provides a unique identifier for models.
'''

from uuid import UUID, uuid4
from pydantic import BaseModel, PrivateAttr, computed_field

class BaseClass(BaseModel):
    '''
    Base class for models that require a unique identifier.
    Use only when you intent to store the model in a database or need to uniquely identify it.

    Attributes:
        id (str): Unique identifier for the model instance.
    '''
    _id: UUID = PrivateAttr(default_factory=uuid4)
    @computed_field
    @property
    def id(self) -> str:
        '''Returns the unique identifier of the model as a string.'''
        return str(self._id)
