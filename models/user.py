from pydantic import BaseModel
from enums.id_type import IdType


class UserBase(BaseModel):
    first_name: str
    last_name: str
    id_type: IdType
    id_number: str
    phone_number: str
    email: str #TODO change to EmailStr from pydantic


class UserUpdate(BaseModel):
    first_name: str

class UserID(UserBase):
    id: int