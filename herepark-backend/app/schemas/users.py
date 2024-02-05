from pydantic import BaseModel


class User(BaseModel):
    username: str
    first_name: str
    last_name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRegistrationData(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
