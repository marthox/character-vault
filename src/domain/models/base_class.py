from pydantic import BaseModel, PrivateAttr, computed_field
from uuid import UUID, uuid4

class BaseClass(BaseModel):
    _id: UUID = PrivateAttr(default_factory=uuid4)
    @computed_field
    @property
    def id(self) -> str:
        return self._id
