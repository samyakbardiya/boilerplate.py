from pydantic import BaseModel


class Status(BaseModel):
    uptime: str
    health: str
