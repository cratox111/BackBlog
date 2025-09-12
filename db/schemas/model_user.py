from pydantic import BaseModel

class UserForm(BaseModel):
    username: str
    name: str
    email: str
    password: str
